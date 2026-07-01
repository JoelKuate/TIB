# 🧪 Tests Logiciels avec l'IA Générative

> Formation professionnelle 2 jours — Utiliser Claude, ChatGPT et Mistral pour automatiser et améliorer les activités de test logiciel.

---

## 📋 Table des matières

1. [Vue d'ensemble](#vue-densemble)
2. [Structure du dossier](#structure-du-dossier)
3. [Par où commencer ?](#par-où-commencer-)
4. [Guide de lecture par profil](#guide-de-lecture-par-profil)
5. [Plan de formation 2 jours](#plan-de-formation-2-jours)
6. [Les ressources en détail](#les-ressources-en-détail)
7. [Démonstration E2E autonome](#démonstration-e2e-autonome)
8. [Prérequis techniques](#prérequis-techniques)

---

## Vue d'ensemble

Ce dépôt contient l'intégralité des ressources d'une formation sur l'**IA générative appliquée aux tests logiciels**. Il couvre 4 chapitres progressifs :

| # | Thème | Niveau |
|---|-------|--------|
| 1 | État d'esprit IA, LLM, ingénierie des prompts | Fondamental |
| 2 | Conception de tests assistée par IA (specs, user stories, Gherkin) | Intermédiaire |
| 3 | Tests unitaires, E2E, agents IA | Avancé |
| 4 | Personnalisation des modèles (RAG, fine-tuning) | Expert |

---

## Structure du dossier

```
tests logiciels/
│
├── 📄 README.md                          ← Vous êtes ici
├── 📄 Programme annoncé.txt              ← Syllabus officiel des 4 chapitres
│
├── ── SUPPORTS DE COURS ──
├── 📕 formation-test-ia-complete-blanc.pdf   ← Support principal (PDF)
├── 📊 rediger-spec-avec-ia-slides.pdf        ← Slides : rédiger des specs avec l'IA
├── 🌐 testeur-fonctionnel-debutant_1.html    ← Module intro (ouvrir dans navigateur)
├── 🌐 jour4-rag-fine-tuning.html             ← Module RAG & Fine-tuning
│
├── ── BIBLIOTHÈQUE DE PROMPTS ──
├── 📝 pack-prompts-qa-guide.md           ← 102 prompts QA + 55 patterns (Markdown)
├── 📝 pack-prompts-qa-guide.docx         ← Idem — version Word (à distribuer)
│
├── ── PLANNING & DOCUMENTATION ──
├── 🗓️ PLAN-FORMATEUR-2-JOURS.html       ← Plan de conduite formateur (ouvrir navigateur)
│
├── ── TESTS E2E AVEC CLAUDE ──
├── 🧪 E2E-CLAUDE-PROMPTS-HYLA.html      ← Prompts E2E pour hyla-air-solution.be
├── 📊 RAPPORT-EXECUTION-E2E-HYLA.html   ← Modèle de rapport d'exécution rempli
├── 🐍 e2e_agent_runner.py               ← Script agent autonome (tests + rapport auto)
│
└── files/
    ├── 📓 bibliotheque-prompts-qa.ipynb      ← 100 prompts interactifs (Jupyter)
    ├── 📋 bibliotheque-prompts-qa.md         ← Idem — version Markdown
    ├── 🗺️ cartographie-documents-test.docx  ← Cartographie des artefacts de test
    ├── 🤖 guide-claude-pour-les-tests.docx  ← Guide prise en main de Claude
    └── 💻 notebook-cycle-complet-test.ipynb ← Exercice fil rouge : cycle complet
```

---

## Par où commencer ?

### 1️⃣ Comprendre le programme

Lire **`Programme annoncé.txt`** — 30 secondes, donne la structure des 4 chapitres.

### 2️⃣ Consulter le plan formateur

Ouvrir **`PLAN-FORMATEUR-2-JOURS.html`** dans un navigateur.  
Ce document est le **chef d'orchestre** : il indique quel fichier utiliser, à quel moment, pendant combien de temps, et pour quel public.

### 3️⃣ Parcourir les prompts

Ouvrir **`pack-prompts-qa-guide.md`** (ou le `.docx` pour les stagiaires).  
102 prompts organisés par activité : exigences → user stories → Gherkin → cas de test → données → rapport.

### 4️⃣ Lancer le Jupyter Notebook

```bash
cd files/
jupyter notebook bibliotheque-prompts-qa.ipynb
```

Les 100 prompts sont exécutables en live avec votre compte ChatGPT / Claude / Mistral.

---

## Guide de lecture par profil

### 👩‍🏫 Formateur

| Priorité | Fichier | Pourquoi |
|----------|---------|----------|
| ⭐⭐⭐ | `PLAN-FORMATEUR-2-JOURS.html` | Vision globale, timing, séquençage |
| ⭐⭐⭐ | `Programme annoncé.txt` | Référence programme officiel |
| ⭐⭐ | `formation-test-ia-complete-blanc.pdf` | Support de cours à projeter |
| ⭐⭐ | `pack-prompts-qa-guide.md` | Navigation rapide entre prompts pendant les TP |
| ⭐ | `e2e_agent_runner.py` | Démo avancée — script agent autonome |

### 🎓 Stagiaire / Apprenant

| Priorité | Fichier | Pourquoi |
|----------|---------|----------|
| ⭐⭐⭐ | `pack-prompts-qa-guide.docx` | Référentiel à conserver après la formation |
| ⭐⭐⭐ | `files/bibliotheque-prompts-qa.ipynb` | Pratiquer les prompts en interactif |
| ⭐⭐ | `files/guide-claude-pour-les-tests.docx` | Prise en main de Claude pour les tests |
| ⭐⭐ | `files/notebook-cycle-complet-test.ipynb` | Exercice fil rouge à refaire seul |
| ⭐ | `E2E-CLAUDE-PROMPTS-HYLA.html` | Modèle de tests E2E à adapter |

### 🧑‍💻 Développeur / Automaticien

| Priorité | Fichier | Pourquoi |
|----------|---------|----------|
| ⭐⭐⭐ | `e2e_agent_runner.py` | Agent de test autonome — à adapter à votre projet |
| ⭐⭐⭐ | `E2E-CLAUDE-PROMPTS-HYLA.html` | Référentiel de prompts E2E (équivalences Playwright) |
| ⭐⭐ | `RAPPORT-EXECUTION-E2E-HYLA.html` | Template de rapport — comprendre la structure |
| ⭐⭐ | `files/bibliotheque-prompts-qa.ipynb` | Prompts pour génération de tests unitaires |

### 🔍 Testeur fonctionnel

| Priorité | Fichier | Pourquoi |
|----------|---------|----------|
| ⭐⭐⭐ | `testeur-fonctionnel-debutant_1.html` | Point d'entrée — ouvrir dans le navigateur |
| ⭐⭐⭐ | `files/cartographie-documents-test.docx` | Vue d'ensemble des artefacts de test |
| ⭐⭐ | `rediger-spec-avec-ia-slides.pdf` | Rédiger specs et user stories avec l'IA |
| ⭐⭐ | `RAPPORT-EXECUTION-E2E-HYLA.html` | Comprendre comment documenter les résultats |

---

## Plan de formation 2 jours

> **Référence complète :** `PLAN-FORMATEUR-2-JOURS.html`

### Jour 1 — Fondamentaux & Techniques de test

| Horaire | Séquence | Fichiers clés |
|---------|----------|---------------|
| 09:00 | Accueil & cadrage | `Programme annoncé.txt` · `cartographie-documents-test.docx` |
| 09:30 | Chapitre 1 — État d'esprit IA, LLM, risques | `formation-test-ia-complete-blanc.pdf` · `testeur-fonctionnel-debutant_1.html` |
| 11:00 | **TP 1** — Premiers prompts | `pack-prompts-qa-guide.docx` · `bibliotheque-prompts-qa.ipynb` |
| 13:00 | Chapitre 2 — Conception de tests avec IA | `rediger-spec-avec-ia-slides.pdf` |
| 14:15 | **TP 2** — User stories, Gherkin, RTM | `bibliotheque-prompts-qa.ipynb` (FN-06 à FN-20) |
| 15:45 | Test exploratoire & données de test | `pack-prompts-qa-guide.md` |
| 17:00 | Synthèse J1 | `guide-claude-pour-les-tests.docx` ← à distribuer |

### Jour 2 — Techniques avancées & Agents IA

| Horaire | Séquence | Fichiers clés |
|---------|----------|---------------|
| 09:20 | **Grand TP** — Cycle complet de test | `notebook-cycle-complet-test.ipynb` |
| 11:00 | Chapitre 3 — Tests unitaires & E2E | `formation-test-ia-complete-blanc.pdf` |
| 12:00 | **TP 3** — Génération tests unitaires/IHM | `bibliotheque-prompts-qa.ipynb` (FN-60 à FN-80) |
| 12:00 | **TP 4** — E2E avec Claude Computer Use | `E2E-CLAUDE-PROMPTS-HYLA.html` · `RAPPORT-EXECUTION-E2E-HYLA.html` · `e2e_agent_runner.py` |
| 13:30 | Chapitre 4 — RAG & Fine-tuning | `jour4-rag-fine-tuning.html` |
| 15:00 | Démonstration live RAG & Fine-tuning | `jour4-rag-fine-tuning.html` |
| 16:45 | Clôture & remise des ressources | Pack complet stagiaires |

---

## Les ressources en détail

### 📕 `formation-test-ia-complete-blanc.pdf`
Support de cours principal. Contient la théorie complète des 4 chapitres. Utilisé comme fond de présentation tout au long des 2 jours.

### 📝 `pack-prompts-qa-guide.md` / `.docx`
**102 prompts QA** organisés par activité + **55 patterns de context engineering**.  
Chaque prompt suit la structure : `Rôle → Tâche → Contexte → Format → Contraintes`.

Catégories couvertes :
- Analyse des exigences (FN-01 à FN-05)
- User stories & épics (FN-06 à FN-10)
- Critères d'acceptation Gherkin (FN-11 à FN-15)
- Matrice de traçabilité RTM (FN-16 à FN-20)
- Conception de cas de test (FN-21 à FN-40)
- Données de test & jeux de données (FN-41 à FN-60)
- Tests unitaires & automatisation (FN-61 à FN-80)
- Analyse de rapports & défauts (FN-81 à FN-100)

### 📓 `files/bibliotheque-prompts-qa.ipynb`
Version **interactive** de la bibliothèque (Jupyter Notebook). Lancer avec `jupyter notebook` et exécuter les cellules en live pendant les TP. Idéal pour la démonstration formateur.

### 💻 `files/notebook-cycle-complet-test.ipynb`
Exercice fil rouge couvrant **le cycle complet** d'un test : exigences → user story → critères Gherkin → cas de test → données → exécution → rapport. À utiliser comme Grand TP du Jour 2 matin.

### 🧪 `E2E-CLAUDE-PROMPTS-HYLA.html`
Référentiel de **22 étapes de test E2E** en langage naturel pour Claude Computer Use, appliqué au site [hyla-air-solution.be](https://hyla-air-solution.be/).  
Chaque étape inclut :
- Le prompt exact à copier dans Claude
- Le résultat attendu
- L'équivalent Playwright (pour la comparaison pédagogique)
- Des conseils formateur

5 scénarios couverts : Navigation, Fiche produit, Panier, Checkout, Cas négatifs.

### 📊 `RAPPORT-EXECUTION-E2E-HYLA.html`
**Modèle de rapport d'exécution** pré-rempli avec des données réalistes.  
Illustre le cycle documentaire complet :

```
Prompt de test → Claude pilote le navigateur → Claude décrit ce qu'il voit
→ Testeur consigne ✅/❌ → Fiches défauts → Avis GO / NO-GO → Signatures
```

Contient : KPI dashboard · tableau de résultats avec réponses Claude · 3 fiches défauts · conclusion.

---

## Démonstration E2E autonome

Le script `e2e_agent_runner.py` permet à Claude d'**exécuter les tests ET de générer le rapport lui-même**, sans intervention humaine.

### Installation

```bash
pip install anthropic
```

### Configuration

```bash
# Windows
set ANTHROPIC_API_KEY=sk-ant-votre-cle

# Linux / macOS
export ANTHROPIC_API_KEY=sk-ant-votre-cle
```

### Exécution

```bash
python e2e_agent_runner.py
```

### Ce que fait le script

```
1. Boucle sur les 10 cas de test définis dans TEST_CASES[]
2. Pour chaque cas : envoie le prompt à Claude Computer Use
3. Claude pilote le navigateur (clics, saisies, screenshots)
4. Claude retourne un JSON structuré { statut, observation, ... }
5. Le script accumule les résultats
6. À la fin : envoie tous les résultats à Claude avec un prompt de mise en forme
7. Claude génère le rapport HTML complet → sauvegardé dans RAPPORT-AUTO-E2E.html
```

### Personnalisation

Pour adapter les tests à un autre site, modifier dans `e2e_agent_runner.py` :

```python
TARGET_URL = "https://votre-site.com/"   # URL cible

TEST_CASES = [
    {
        "id": "TC-01",
        "scenario": "SC-01 – Mon scénario",
        "titre": "Description courte",
        "prompt": "Votre prompt en langage naturel..."
    },
    # ...
]
```

---

## Prérequis techniques

### Pour les supports HTML
Ouvrir directement dans un navigateur moderne (Chrome, Edge, Firefox).  
Aucune installation requise.

### Pour les Notebooks Jupyter

```bash
pip install jupyter
jupyter notebook
```

### Pour le script E2E agent

```bash
pip install anthropic          # SDK Anthropic
# + Compte Anthropic avec accès API Claude Computer Use
# + ANTHROPIC_API_KEY définie en variable d'environnement
```

### Comptes IA recommandés pour les TP
- [Claude](https://claude.ai) — recommandé (Computer Use disponible)
- [ChatGPT](https://chat.openai.com) — alternative
- [Mistral](https://chat.mistral.ai) — alternative open-source

---

## Licence

Ressources pédagogiques à usage de formation. Contenu à adapter à votre contexte avant tout usage en production.

---

*Formation réalisée avec [KUATE JOEL PARFAIT]([https://claude.ai/code](https://www.linkedin.com/in/joelparfaitkuate/)) — Orsys*
