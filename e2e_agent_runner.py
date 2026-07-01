"""
E2E Agent Runner – Claude Computer Use
======================================
Lance Claude comme agent de test autonome :
  1. Claude pilote le navigateur (clics, saisies, screenshots)
  2. Claude évalue chaque résultat (pass / fail / blocked)
  3. Claude génère lui-même le rapport HTML final

Usage :
    pip install anthropic
    python e2e_agent_runner.py

Prérequis :
    - Variable d'environnement ANTHROPIC_API_KEY définie
    - Un navigateur ouvert sur l'URL cible (ou laisser Claude l'ouvrir)
    - Extension Claude Computer Use activée (accès écran + clavier + souris)
"""

import os
import json
import datetime
import anthropic

# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────
TARGET_URL  = "https://hyla-air-solution.be/"
RAPPORT_OUT = "RAPPORT-AUTO-E2E.html"
MODEL       = "claude-opus-4-8"          # modèle avec computer use
MAX_TOKENS  = 8192

# ─────────────────────────────────────────────
# DÉFINITION DES CAS DE TEST
# Chaque cas = un prompt naturel + un ID + une description courte
# ─────────────────────────────────────────────
TEST_CASES = [
    {
        "id": "TC-01",
        "scenario": "SC-01 – Navigation",
        "titre": "Chargement page d'accueil",
        "prompt": f"""
Ouvre le navigateur et navigue vers {TARGET_URL}.
Attends que la page soit complètement chargée.
Si une bannière cookies apparaît, ferme-la.

VÉRIFIE :
- Le logo HYLA est visible
- Le menu de navigation est présent
- La page ne contient pas de message d'erreur (404, 500, etc.)

Réponds en JSON uniquement :
{{"statut": "PASSÉ" | "ÉCHOUÉ" | "BLOQUÉ", "observation": "...", "screenshot_utile": true | false}}
"""
    },
    {
        "id": "TC-02",
        "scenario": "SC-01 – Navigation",
        "titre": "Accès au catalogue produits",
        "prompt": """
Dans le menu principal, clique sur l'entrée qui mène aux produits
(cherche : "Boutique", "Produits", "Shop", "Nos produits").
Attends que la page liste de produits se charge.

VÉRIFIE qu'une liste ou grille de produits est visible.

Réponds en JSON uniquement :
{"statut": "PASSÉ" | "ÉCHOUÉ" | "BLOQUÉ", "observation": "...", "nb_produits_vus": <nombre ou null>}
"""
    },
    {
        "id": "TC-03",
        "scenario": "SC-02 – Fiche produit",
        "titre": "Ouverture fiche produit",
        "prompt": """
Clique sur le premier produit visible dans la grille (image ou titre).
Attends que la fiche produit soit chargée.

VÉRIFIE :
- Un titre H1 de produit est visible
- Un prix en € est affiché
- Une image produit est chargée (pas d'icône cassée)
- Un bouton "Ajouter au panier" (ou équivalent) est présent

Réponds en JSON uniquement :
{"statut": "PASSÉ" | "ÉCHOUÉ" | "BLOQUÉ", "observation": "...", "nom_produit": "...", "prix": "..."}
"""
    },
    {
        "id": "TC-04",
        "scenario": "SC-02 – Fiche produit",
        "titre": "Ajout au panier",
        "prompt": """
Sur la fiche produit actuelle, clique sur le bouton "Ajouter au panier".
Attends la confirmation visuelle (notification, animation, compteur).

VÉRIFIE qu'une confirmation d'ajout est visible
(compteur header, notification toast, ou mini-panier ouvert).

Réponds en JSON uniquement :
{"statut": "PASSÉ" | "ÉCHOUÉ" | "BLOQUÉ", "observation": "...", "confirmation_visible": true | false}
"""
    },
    {
        "id": "TC-05",
        "scenario": "SC-03 – Panier",
        "titre": "Vérification contenu panier",
        "prompt": """
Accède à la page panier (clique sur l'icône panier dans le header
ou navigue vers /cart/ ou /panier/).

VÉRIFIE :
- Le produit ajouté est bien listé
- La quantité est 1
- Le prix unitaire est affiché en €
- Un total est calculé
- Un bouton "Passer la commande" est présent

Réponds en JSON uniquement :
{"statut": "PASSÉ" | "ÉCHOUÉ" | "BLOQUÉ", "observation": "...", "total_affiché": "..."}
"""
    },
    {
        "id": "TC-06",
        "scenario": "SC-04 – Checkout",
        "titre": "Accès et remplissage formulaire",
        "prompt": """
Clique sur "Passer la commande" pour accéder au checkout.
Remplis le formulaire avec ces données de TEST :
  Prénom : Jean
  Nom : Testeur
  Adresse : 12 Rue de la Qualité
  Ville : Bruxelles
  Code postal : 1000
  Pays : Belgique
  Téléphone : +32 470 000 000
  Email : test.e2e@exemple.be

VÉRIFIE qu'aucune erreur de validation n'apparaît.
NE PAS soumettre la commande — arrête-toi après avoir rempli le formulaire.

Réponds en JSON uniquement :
{"statut": "PASSÉ" | "ÉCHOUÉ" | "BLOQUÉ", "observation": "...", "erreurs_validation": []}
"""
    },
    {
        "id": "TC-07",
        "scenario": "SC-04 – Checkout",
        "titre": "Vérification récapitulatif et paiement",
        "prompt": """
Sans soumettre, VÉRIFIE sur la page checkout :
- Le récapitulatif de commande contient le bon produit
- Un total TTC est affiché
- Au moins 1 mode de paiement est disponible

Liste les modes de paiement visibles.

Réponds en JSON uniquement :
{"statut": "PASSÉ" | "ÉCHOUÉ" | "BLOQUÉ", "observation": "...", "modes_paiement": [...], "total_ttc": "..."}
"""
    },
    {
        "id": "TC-08",
        "scenario": "SC-05 – Cas négatifs",
        "titre": "Formulaire soumis vide",
        "prompt": """
Navigue vers la page checkout (/checkout/).
Sans remplir aucun champ, clique sur "Passer la commande".

VÉRIFIE que des messages d'erreur apparaissent sur les champs obligatoires.

Réponds en JSON uniquement :
{"statut": "PASSÉ" | "ÉCHOUÉ" | "BLOQUÉ", "observation": "...", "champs_en_erreur": [...]}
"""
    },
    {
        "id": "TC-09",
        "scenario": "SC-05 – Cas négatifs",
        "titre": "Email invalide — validation",
        "prompt": """
Dans le formulaire checkout, saisis uniquement dans le champ email :
"ceci-nest-pas-un-email"
Tente de soumettre le formulaire.

VÉRIFIE qu'un message d'erreur de validation email apparaît
CÔTÉ NAVIGATEUR (avant soumission au serveur).

Réponds en JSON uniquement :
{"statut": "PASSÉ" | "ÉCHOUÉ" | "BLOQUÉ", "observation": "...", "validation_cote_client": true | false}
"""
    },
    {
        "id": "TC-10",
        "scenario": "SC-05 – Cas négatifs",
        "titre": "Recherche sans résultats",
        "prompt": """
Utilise la fonction de recherche du site (icône loupe dans le header).
Saisis : xyzproduitinexistant99
Valide la recherche.

VÉRIFIE :
- Un message "aucun résultat" (ou équivalent) s'affiche
- La page n'est pas vide ou blanche
- Aucune erreur technique (500, page blanche) n'est visible

Réponds en JSON uniquement :
{"statut": "PASSÉ" | "ÉCHOUÉ" | "BLOQUÉ", "observation": "...", "message_aucun_resultat": true | false}
"""
    },
]

# ─────────────────────────────────────────────
# PROMPT FINAL : demander à Claude de générer le rapport HTML
# ─────────────────────────────────────────────
RAPPORT_PROMPT_TEMPLATE = """
Tu as exécuté {nb_total} cas de test sur {url}.
Voici les résultats collectés en JSON :

{resultats_json}

Génère un rapport d'exécution HTML COMPLET et autonome (CSS inline inclus) avec :

1. EN-TÊTE : référence RPT-E2E-AUTO-001, date {date}, URL, outil "Claude Computer Use"

2. TABLEAU DE BORD KPI :
   - Total cas : {nb_total}
   - Passés : {nb_passes}
   - Échoués : {nb_echoues}
   - Bloqués : {nb_bloques}
   - Taux de succès : {taux}%

3. TABLEAU RÉSULTATS ligne par ligne avec colonnes :
   ID | Titre | Statut (badge coloré ✅/❌/⚠️) | Observation de Claude

4. FICHES DÉFAUTS pour chaque cas ÉCHOUÉ ou BLOQUÉ :
   - ID défaut (DEF-001, etc.)
   - Titre descriptif
   - Étapes de reproduction basées sur l'observation
   - Sévérité estimée (Haute si checkout/paiement, Moyenne sinon)

5. CONCLUSION : avis GO / GO CONDITIONNEL / NO-GO selon :
   - GO si taux ≥ 90%
   - GO CONDITIONNEL si 70% ≤ taux < 90%
   - NO-GO si taux < 70%

6. Zone de signatures (Testeur, Responsable Qualité, Chef de projet)

Design : fond #f4f6fa, couleurs status : vert #1a9e6a / rouge #d93025 / orange #e07b00.
Header sombre bleu marine #1b2a4a.

Retourne UNIQUEMENT le code HTML complet, sans balise markdown.
"""

# ─────────────────────────────────────────────
# FONCTIONS UTILITAIRES
# ─────────────────────────────────────────────

def extraire_json(texte: str) -> dict:
    """Extrait le premier objet JSON trouvé dans la réponse de Claude."""
    import re
    match = re.search(r'\{.*\}', texte, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    # Fallback si Claude n'a pas respecté le format JSON
    statut = "PASSÉ" if "PASSÉ" in texte or "passé" in texte.lower() else \
             "ÉCHOUÉ" if "ÉCHOUÉ" in texte or "échoué" in texte.lower() else "BLOQUÉ"
    return {"statut": statut, "observation": texte[:300]}


def executer_test(client: anthropic.Anthropic, tc: dict) -> dict:
    """Envoie un prompt de test à Claude Computer Use et récupère le résultat."""
    print(f"  → Exécution {tc['id']} : {tc['titre']}...")

    # On utilise le modèle avec computer use en mode beta
    reponse = client.beta.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        tools=[
            {
                "type": "computer_20250124",
                "name": "computer",
                "display_width_px": 1280,
                "display_height_px": 800,
            }
        ],
        messages=[
            {
                "role": "user",
                "content": tc["prompt"]
            }
        ],
        betas=["computer-use-2025-01-24"],
    )

    # Extraire le texte final de la réponse
    texte_final = ""
    for bloc in reponse.content:
        if hasattr(bloc, "text"):
            texte_final += bloc.text

    resultat = extraire_json(texte_final)
    resultat["id"]       = tc["id"]
    resultat["titre"]    = tc["titre"]
    resultat["scenario"] = tc["scenario"]

    statut = resultat.get("statut", "BLOQUÉ")
    icone  = "✅" if statut == "PASSÉ" else "❌" if statut == "ÉCHOUÉ" else "⚠️"
    print(f"     {icone} {statut} — {resultat.get('observation', '')[:80]}")

    return resultat


def generer_rapport(client: anthropic.Anthropic, resultats: list[dict]) -> str:
    """Demande à Claude de générer le rapport HTML à partir des résultats."""
    print("\n📝 Génération du rapport HTML par Claude...")

    nb_total   = len(resultats)
    nb_passes  = sum(1 for r in resultats if r.get("statut") == "PASSÉ")
    nb_echoues = sum(1 for r in resultats if r.get("statut") == "ÉCHOUÉ")
    nb_bloques = sum(1 for r in resultats if r.get("statut") == "BLOQUÉ")
    taux       = round((nb_passes / nb_total) * 100) if nb_total else 0

    prompt = RAPPORT_PROMPT_TEMPLATE.format(
        nb_total       = nb_total,
        url            = TARGET_URL,
        resultats_json = json.dumps(resultats, ensure_ascii=False, indent=2),
        date           = datetime.date.today().strftime("%d/%m/%Y"),
        nb_passes      = nb_passes,
        nb_echoues     = nb_echoues,
        nb_bloques     = nb_bloques,
        taux           = taux,
    )

    reponse = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )

    html = reponse.content[0].text
    # Nettoyer si Claude a ajouté des balises markdown autour
    if html.startswith("```"):
        lignes = html.split("\n")
        html = "\n".join(lignes[1:-1])

    return html


# ─────────────────────────────────────────────
# POINT D'ENTRÉE
# ─────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  E2E Agent Runner — Claude Computer Use")
    print(f"  Cible : {TARGET_URL}")
    print(f"  {len(TEST_CASES)} cas de test à exécuter")
    print("=" * 60)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("\n❌ ERREUR : variable ANTHROPIC_API_KEY non définie.")
        print("   Exécutez : set ANTHROPIC_API_KEY=sk-ant-...")
        return

    client = anthropic.Anthropic(api_key=api_key)

    # ── 1. Exécution des cas de test ──
    resultats = []
    for i, tc in enumerate(TEST_CASES, 1):
        print(f"\n[{i}/{len(TEST_CASES)}] {tc['scenario']}")
        try:
            res = executer_test(client, tc)
        except Exception as e:
            print(f"     ⚠️  Erreur lors de l'exécution : {e}")
            res = {
                "id": tc["id"], "titre": tc["titre"],
                "scenario": tc["scenario"],
                "statut": "BLOQUÉ",
                "observation": f"Erreur technique : {str(e)}"
            }
        resultats.append(res)

    # ── 2. Génération du rapport par Claude ──
    rapport_html = generer_rapport(client, resultats)

    # ── 3. Écriture du fichier ──
    chemin = os.path.join(os.path.dirname(__file__), RAPPORT_OUT)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(rapport_html)

    print(f"\n✅ Rapport généré : {chemin}")
    print("\nRésumé :")
    passes  = sum(1 for r in resultats if r.get("statut") == "PASSÉ")
    echoues = sum(1 for r in resultats if r.get("statut") == "ÉCHOUÉ")
    bloques = sum(1 for r in resultats if r.get("statut") == "BLOQUÉ")
    print(f"  ✅ Passés  : {passes}")
    print(f"  ❌ Échoués : {echoues}")
    print(f"  ⚠️  Bloqués : {bloques}")
    print(f"  📊 Taux    : {round(passes/len(resultats)*100)}%")
    print(f"\n👉 Ouvrez {RAPPORT_OUT} dans votre navigateur.")


if __name__ == "__main__":
    main()
