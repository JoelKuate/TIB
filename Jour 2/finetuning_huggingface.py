"""
Fine-tuning d'un modele Hugging Face avec LoRA (PEFT)
Digital House Company - Formation IA - hello@dhcompany.pro

Ce script accompagne le support de formation "Fine-tuning des modeles IA avec
Hugging Face" (slides-finetuning-huggingface.html). Il reprend, dans un seul
fichier executable, l'integralite du parcours enseigne :

  1. Chargement d'un dataset depuis le Hub                (Module 03)
  2. Chargement d'un modele pre-entraine + tokenizer       (Modules 02 et 04)
  3. Tokenisation et preparation train/eval                (Module 03)
  4. Configuration LoRA - fine-tuning leger                (Module 05)
  5. Entrainement avec le Trainer                          (Module 04)
  6. Evaluation avant/apres et metriques                   (Module 06)
  7. Sauvegarde locale et partage optionnel sur le Hub      (Module 07)

Modele utilise : distilbert-base-uncased (66 millions de parametres) - assez
leger pour tourner sur un ordinateur portable, sans GPU dedie.
Tache : classification de sentiment binaire (positif / negatif) sur un
sous-ensemble reduit de SST-2 (Stanford Sentiment Treebank), un dataset
standard, deja utilise dans de nombreux tutoriels Hugging Face.

Note pedagogique sur LoRA : sur un modele aussi petit que DistilBERT, LoRA
n'est pas strictement necessaire (un full fine-tuning tiendrait deja en
memoire). Il est utilise ici pour illustrer concretement la configuration
vue au Module 05 du cours - exactement la meme demarche s'applique telle
quelle a des modeles bien plus gros (Llama, Mistral...), ou LoRA devient
alors indispensable pour tenir en memoire GPU.

Installation :
    pip install -r requirements-finetuning.txt

Lancement :
    python finetuning_huggingface.py
"""

import numpy as np
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    pipeline,
)
from peft import LoraConfig, get_peft_model, TaskType
import evaluate


# ──────────────────────────────────────────────────────────────────────────
# Parametres modifiables — a ajuster selon la puissance de la machine
# et le temps disponible pendant la formation.
# ──────────────────────────────────────────────────────────────────────────
MODEL_NAME = "distilbert-base-uncased"
NOMBRE_EXEMPLES_ENTRAINEMENT = 2000   # sous-ensemble reduit pour une demo rapide
NOMBRE_EXEMPLES_EVALUATION = 500
DOSSIER_SORTIE = "./modele-finetune-sentiment"
NOMBRE_EPOCHS = 3


def charger_modele():
    """
    Etape 1 — Charger le modele pre-entraine et son tokenizer (Modules 02 et 04).

    AutoModelForSequenceClassification ajoute automatiquement, au-dessus du
    modele de base, une petite couche de classification a 2 sorties
    (num_labels=2 : negatif / positif).
    """
    print(f"[1/6] Chargement du modele de base : {MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)
    return model, tokenizer


def charger_donnees(tokenizer):
    """
    Etape 2 — Charger et tokeniser le dataset (Module 03).

    SST-2 fournit des phrases en anglais etiquetees 0 (negatif) ou 1 (positif).
    Le split "test" de GLUE n'a pas de vraies etiquettes (elles sont cachees
    pour le classement officiel) : on utilise donc "validation" pour evaluer.
    """
    print("[2/6] Chargement du dataset SST-2 depuis le Hub Hugging Face...")
    dataset = load_dataset("glue", "sst2")

    # On reduit volontairement la taille pour que la demo tourne en quelques
    # minutes sur un ordinateur portable. En conditions reelles de production,
    # on utiliserait l'integralite du dataset disponible.
    train_dataset = dataset["train"].shuffle(seed=42).select(range(NOMBRE_EXEMPLES_ENTRAINEMENT))
    taille_eval = min(NOMBRE_EXEMPLES_EVALUATION, len(dataset["validation"]))
    eval_dataset = dataset["validation"].shuffle(seed=42).select(range(taille_eval))

    def tokeniser(exemples):
        return tokenizer(exemples["sentence"], padding="max_length", truncation=True, max_length=128)

    print("    Tokenisation des phrases (transformation texte -> nombres)...")
    train_dataset = train_dataset.map(tokeniser, batched=True)
    eval_dataset = eval_dataset.map(tokeniser, batched=True)

    print(f"    {len(train_dataset)} exemples d'entrainement, {len(eval_dataset)} exemples d'evaluation.")
    return train_dataset, eval_dataset


def appliquer_lora(model):
    """
    Etape 3 — Appliquer LoRA pour n'entrainer qu'une petite fraction des
    parametres du modele (Module 05).

    target_modules cible les couches d'attention "query" et "value" de
    DistilBERT (nommees q_lin / v_lin dans cette architecture — sur un
    modele type Llama/Mistral, ces memes couches s'appellent q_proj/v_proj,
    comme vu dans le support de cours).
    """
    print("[3/6] Configuration de LoRA (fine-tuning leger)...")
    lora_config = LoraConfig(
        task_type=TaskType.SEQ_CLS,
        r=8,                 # rang des matrices LoRA ajoutees
        lora_alpha=16,        # facteur d'echelle de l'ajustement LoRA
        lora_dropout=0.1,     # regularisation, limite le surapprentissage
        target_modules=["q_lin", "v_lin"],
    )
    model = get_peft_model(model, lora_config)

    # Affiche concretement le gain : combien de parametres sont reellement
    # entraines par rapport au total du modele (voir slide 05.5 du cours).
    model.print_trainable_parameters()
    return model


def calculer_metriques(eval_pred):
    """
    Fonction appelee automatiquement par le Trainer apres chaque evaluation
    (Module 06). Calcule l'accuracy : proportion de predictions correctes.
    """
    metrique_accuracy = evaluate.load("accuracy")
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metrique_accuracy.compute(predictions=predictions, references=labels)


def entrainer(model, train_dataset, eval_dataset):
    """
    Etape 4 — Configurer et lancer l'entrainement (Module 04).

    Remarque de version : selon la version de la bibliotheque `transformers`
    installee, ce parametre peut s'appeler `eval_strategy` (recent) ou
    `evaluation_strategy` (plus ancien). Si une erreur mentionne ce nom,
    essayez l'autre orthographe.
    """
    print("[4/6] Preparation de l'entrainement...")
    training_args = TrainingArguments(
        output_dir=DOSSIER_SORTIE,
        num_train_epochs=NOMBRE_EPOCHS,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        learning_rate=2e-4,        # un peu plus eleve qu'en full fine-tuning : normal avec LoRA
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_steps=20,
        load_best_model_at_end=True,
        report_to="none",          # desactive l'envoi vers wandb/tensorboard par defaut
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        compute_metrics=calculer_metriques,
    )

    print("[5/6] Demarrage de l'entrainement (cela peut prendre plusieurs minutes)...\n")
    trainer.train()
    return trainer


def comparer_sur_exemples(tokenizer, trainer):
    """
    Etape 5 — Tester le modele fine-tune sur des phrases jamais vues,
    pour verifier concretement ce qu'il a appris (Module 06).
    """
    phrases_test = [
        "This movie was absolutely wonderful, I loved every minute of it.",
        "What a waste of time, the plot made no sense at all.",
        "The acting was decent but the story felt quite predictable.",
    ]

    classifieur = pipeline(
        "text-classification",
        model=trainer.model,
        tokenizer=tokenizer,
        device=-1,  # -1 = CPU ; remplacer par 0 pour utiliser un GPU disponible
    )

    print("\n=== Resultats sur des phrases jamais vues a l'entrainement ===")
    for phrase in phrases_test:
        resultat = classifieur(phrase)[0]
        label = "POSITIF" if resultat["label"] == "LABEL_1" else "NEGATIF"
        print(f'  {label:8s} ({resultat["score"]:.1%})  —  "{phrase}"')


def main():
    model, tokenizer = charger_modele()
    train_dataset, eval_dataset = charger_donnees(tokenizer)
    model = appliquer_lora(model)

    trainer = entrainer(model, train_dataset, eval_dataset)

    print("\n[6/6] Evaluation finale et sauvegarde...")
    resultats_finaux = trainer.evaluate()
    print(f"    Accuracy finale sur le jeu d'evaluation : {resultats_finaux['eval_accuracy']:.1%}")

    comparer_sur_exemples(tokenizer, trainer)

    print(f"\nSauvegarde du modele fine-tune dans : {DOSSIER_SORTIE}")
    trainer.save_model(DOSSIER_SORTIE)
    tokenizer.save_pretrained(DOSSIER_SORTIE)

    # Pour partager le modele sur le Hub Hugging Face (Module 07 du cours),
    # decommentez ces deux lignes apres vous etre connecte avec :
    #     huggingface-cli login
    #
    # trainer.model.push_to_hub("votre-compte/mon-modele-sentiment-lora")
    # tokenizer.push_to_hub("votre-compte/mon-modele-sentiment-lora")

    print("\nTermine.")


if __name__ == "__main__":
    main()
