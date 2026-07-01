# Bibliothèque de prompts — Test fonctionnel assisté par IA

Digital House Company · hello@dhcompany.pro

## 100 prompts structurés (FN-01 à FN-100)

### FN-01 — Cahier des charges / spécifications — Génération initiale [Cahier des charges / spécifications]

- **Rôle** : analyste QA spécialisé en revue de spécifications.
- **Tâche** : génère le cahier des charges à partir des informations fournies ci-dessous.
- **Contexte** : Un extrait de cahier des charges — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-02 — Cahier des charges / spécifications — Cas limites et zones de risque [Cahier des charges / spécifications]

- **Rôle** : analyste QA spécialisé en revue de spécifications.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le cahier des charges fourni, et complète-le.
- **Contexte** : Un extrait de cahier des charges déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-03 — Cahier des charges / spécifications — Restitution en tableau structuré [Cahier des charges / spécifications]

- **Rôle** : analyste QA spécialisé en revue de spécifications.
- **Tâche** : restitue le cahier des charges sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Un extrait de cahier des charges, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-04 — Cahier des charges / spécifications — Audit et revue de conformité [Cahier des charges / spécifications]

- **Rôle** : analyste QA spécialisé en revue de spécifications, en posture d'audit qualité.
- **Tâche** : relis le cahier des charges fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Un extrait de cahier des charges, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-05 — Cahier des charges / spécifications — Adaptation à un autre contexte métier [Cahier des charges / spécifications]

- **Rôle** : analyste QA spécialisé en revue de spécifications.
- **Tâche** : adapte ce modèle de le cahier des charges (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Un extrait de cahier des charges existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-06 — User stories — Génération initiale [User stories]

- **Rôle** : Product Owner assisté d'un testeur.
- **Tâche** : génère la user story à partir des informations fournies ci-dessous.
- **Contexte** : Une fonctionnalité à décrire — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-07 — User stories — Cas limites et zones de risque [User stories]

- **Rôle** : Product Owner assisté d'un testeur.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans la user story fourni, et complète-le.
- **Contexte** : Une fonctionnalité à décrire déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-08 — User stories — Restitution en tableau structuré [User stories]

- **Rôle** : Product Owner assisté d'un testeur.
- **Tâche** : restitue la user story sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Une fonctionnalité à décrire, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-09 — User stories — Audit et revue de conformité [User stories]

- **Rôle** : Product Owner assisté d'un testeur, en posture d'audit qualité.
- **Tâche** : relis la user story fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Une fonctionnalité à décrire, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-10 — User stories — Adaptation à un autre contexte métier [User stories]

- **Rôle** : Product Owner assisté d'un testeur.
- **Tâche** : adapte ce modèle de la user story (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Une fonctionnalité à décrire existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-11 — Critères d'acceptation Gherkin — Génération initiale [Critères d'acceptation Gherkin]

- **Rôle** : analyste QA, spécialiste recette métier.
- **Tâche** : génère les critères d'acceptation Gherkin à partir des informations fournies ci-dessous.
- **Contexte** : Une user story — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-12 — Critères d'acceptation Gherkin — Cas limites et zones de risque [Critères d'acceptation Gherkin]

- **Rôle** : analyste QA, spécialiste recette métier.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans les critères d'acceptation Gherkin fourni, et complète-le.
- **Contexte** : Une user story déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-13 — Critères d'acceptation Gherkin — Restitution en tableau structuré [Critères d'acceptation Gherkin]

- **Rôle** : analyste QA, spécialiste recette métier.
- **Tâche** : restitue les critères d'acceptation Gherkin sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Une user story, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-14 — Critères d'acceptation Gherkin — Audit et revue de conformité [Critères d'acceptation Gherkin]

- **Rôle** : analyste QA, spécialiste recette métier, en posture d'audit qualité.
- **Tâche** : relis les critères d'acceptation Gherkin fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Une user story, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-15 — Critères d'acceptation Gherkin — Adaptation à un autre contexte métier [Critères d'acceptation Gherkin]

- **Rôle** : analyste QA, spécialiste recette métier.
- **Tâche** : adapte ce modèle de les critères d'acceptation Gherkin (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Une user story existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-16 — Matrice de traçabilité (RTM) — Génération initiale [Matrice de traçabilité (RTM)]

- **Rôle** : Test Analyst.
- **Tâche** : génère la matrice de traçabilité à partir des informations fournies ci-dessous.
- **Contexte** : Une liste d'exigences et de cas de test — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-17 — Matrice de traçabilité (RTM) — Cas limites et zones de risque [Matrice de traçabilité (RTM)]

- **Rôle** : Test Analyst.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans la matrice de traçabilité fourni, et complète-le.
- **Contexte** : Une liste d'exigences et de cas de test déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-18 — Matrice de traçabilité (RTM) — Restitution en tableau structuré [Matrice de traçabilité (RTM)]

- **Rôle** : Test Analyst.
- **Tâche** : restitue la matrice de traçabilité sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Une liste d'exigences et de cas de test, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-19 — Matrice de traçabilité (RTM) — Audit et revue de conformité [Matrice de traçabilité (RTM)]

- **Rôle** : Test Analyst, en posture d'audit qualité.
- **Tâche** : relis la matrice de traçabilité fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Une liste d'exigences et de cas de test, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-20 — Matrice de traçabilité (RTM) — Adaptation à un autre contexte métier [Matrice de traçabilité (RTM)]

- **Rôle** : Test Analyst.
- **Tâche** : adapte ce modèle de la matrice de traçabilité (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Une liste d'exigences et de cas de test existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-21 — Stratégie de test — Génération initiale [Stratégie de test]

- **Rôle** : Test Manager.
- **Tâche** : génère la stratégie de test à partir des informations fournies ci-dessous.
- **Contexte** : Une liste de fonctionnalités à prioriser par risque — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-22 — Stratégie de test — Cas limites et zones de risque [Stratégie de test]

- **Rôle** : Test Manager.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans la stratégie de test fourni, et complète-le.
- **Contexte** : Une liste de fonctionnalités à prioriser par risque déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-23 — Stratégie de test — Restitution en tableau structuré [Stratégie de test]

- **Rôle** : Test Manager.
- **Tâche** : restitue la stratégie de test sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Une liste de fonctionnalités à prioriser par risque, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-24 — Stratégie de test — Audit et revue de conformité [Stratégie de test]

- **Rôle** : Test Manager, en posture d'audit qualité.
- **Tâche** : relis la stratégie de test fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Une liste de fonctionnalités à prioriser par risque, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-25 — Stratégie de test — Adaptation à un autre contexte métier [Stratégie de test]

- **Rôle** : Test Manager.
- **Tâche** : adapte ce modèle de la stratégie de test (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Une liste de fonctionnalités à prioriser par risque existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-26 — Plan de test (IEEE 829) — Génération initiale [Plan de test (IEEE 829)]

- **Rôle** : Test Manager.
- **Tâche** : génère le plan de test à partir des informations fournies ci-dessous.
- **Contexte** : Un module et son contexte projet — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-27 — Plan de test (IEEE 829) — Cas limites et zones de risque [Plan de test (IEEE 829)]

- **Rôle** : Test Manager.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le plan de test fourni, et complète-le.
- **Contexte** : Un module et son contexte projet déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-28 — Plan de test (IEEE 829) — Restitution en tableau structuré [Plan de test (IEEE 829)]

- **Rôle** : Test Manager.
- **Tâche** : restitue le plan de test sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Un module et son contexte projet, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-29 — Plan de test (IEEE 829) — Audit et revue de conformité [Plan de test (IEEE 829)]

- **Rôle** : Test Manager, en posture d'audit qualité.
- **Tâche** : relis le plan de test fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Un module et son contexte projet, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-30 — Plan de test (IEEE 829) — Adaptation à un autre contexte métier [Plan de test (IEEE 829)]

- **Rôle** : Test Manager.
- **Tâche** : adapte ce modèle de le plan de test (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Un module et son contexte projet existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-31 — Analyse de risques qualité — Génération initiale [Analyse de risques qualité]

- **Rôle** : Test Manager.
- **Tâche** : génère l'analyse de risques à partir des informations fournies ci-dessous.
- **Contexte** : Une liste de fonctionnalités et leur criticité métier — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-32 — Analyse de risques qualité — Cas limites et zones de risque [Analyse de risques qualité]

- **Rôle** : Test Manager.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans l'analyse de risques fourni, et complète-le.
- **Contexte** : Une liste de fonctionnalités et leur criticité métier déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-33 — Analyse de risques qualité — Restitution en tableau structuré [Analyse de risques qualité]

- **Rôle** : Test Manager.
- **Tâche** : restitue l'analyse de risques sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Une liste de fonctionnalités et leur criticité métier, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-34 — Analyse de risques qualité — Audit et revue de conformité [Analyse de risques qualité]

- **Rôle** : Test Manager, en posture d'audit qualité.
- **Tâche** : relis l'analyse de risques fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Une liste de fonctionnalités et leur criticité métier, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-35 — Analyse de risques qualité — Adaptation à un autre contexte métier [Analyse de risques qualité]

- **Rôle** : Test Manager.
- **Tâche** : adapte ce modèle de l'analyse de risques (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Une liste de fonctionnalités et leur criticité métier existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-36 — Test Design Specification — Génération initiale [Test Design Specification]

- **Rôle** : Test Analyst.
- **Tâche** : génère la spécification de conception des tests à partir des informations fournies ci-dessous.
- **Contexte** : Une exigence ou une fonction à tester — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-37 — Test Design Specification — Cas limites et zones de risque [Test Design Specification]

- **Rôle** : Test Analyst.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans la spécification de conception des tests fourni, et complète-le.
- **Contexte** : Une exigence ou une fonction à tester déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-38 — Test Design Specification — Restitution en tableau structuré [Test Design Specification]

- **Rôle** : Test Analyst.
- **Tâche** : restitue la spécification de conception des tests sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Une exigence ou une fonction à tester, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-39 — Test Design Specification — Audit et revue de conformité [Test Design Specification]

- **Rôle** : Test Analyst, en posture d'audit qualité.
- **Tâche** : relis la spécification de conception des tests fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Une exigence ou une fonction à tester, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-40 — Test Design Specification — Adaptation à un autre contexte métier [Test Design Specification]

- **Rôle** : Test Analyst.
- **Tâche** : adapte ce modèle de la spécification de conception des tests (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Une exigence ou une fonction à tester existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-41 — Cas de test (Test Case) — Génération initiale [Cas de test (Test Case)]

- **Rôle** : testeur QA senior.
- **Tâche** : génère les cas de test à partir des informations fournies ci-dessous.
- **Contexte** : Des conditions de test déjà identifiées — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-42 — Cas de test (Test Case) — Cas limites et zones de risque [Cas de test (Test Case)]

- **Rôle** : testeur QA senior.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans les cas de test fourni, et complète-le.
- **Contexte** : Des conditions de test déjà identifiées déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-43 — Cas de test (Test Case) — Restitution en tableau structuré [Cas de test (Test Case)]

- **Rôle** : testeur QA senior.
- **Tâche** : restitue les cas de test sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Des conditions de test déjà identifiées, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-44 — Cas de test (Test Case) — Audit et revue de conformité [Cas de test (Test Case)]

- **Rôle** : testeur QA senior, en posture d'audit qualité.
- **Tâche** : relis les cas de test fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Des conditions de test déjà identifiées, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-45 — Cas de test (Test Case) — Adaptation à un autre contexte métier [Cas de test (Test Case)]

- **Rôle** : testeur QA senior.
- **Tâche** : adapte ce modèle de les cas de test (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Des conditions de test déjà identifiées existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-46 — Procédures de test / séquencement — Génération initiale [Procédures de test / séquencement]

- **Rôle** : testeur QA.
- **Tâche** : génère la procédure de test à partir des informations fournies ci-dessous.
- **Contexte** : Un ensemble de cas de test à enchaîner — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-47 — Procédures de test / séquencement — Cas limites et zones de risque [Procédures de test / séquencement]

- **Rôle** : testeur QA.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans la procédure de test fourni, et complète-le.
- **Contexte** : Un ensemble de cas de test à enchaîner déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-48 — Procédures de test / séquencement — Restitution en tableau structuré [Procédures de test / séquencement]

- **Rôle** : testeur QA.
- **Tâche** : restitue la procédure de test sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Un ensemble de cas de test à enchaîner, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-49 — Procédures de test / séquencement — Audit et revue de conformité [Procédures de test / séquencement]

- **Rôle** : testeur QA, en posture d'audit qualité.
- **Tâche** : relis la procédure de test fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Un ensemble de cas de test à enchaîner, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-50 — Procédures de test / séquencement — Adaptation à un autre contexte métier [Procédures de test / séquencement]

- **Rôle** : testeur QA.
- **Tâche** : adapte ce modèle de la procédure de test (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Un ensemble de cas de test à enchaîner existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-51 — Jeux de données de test — Génération initiale [Jeux de données de test]

- **Rôle** : testeur QA.
- **Tâche** : génère le jeu de données de test à partir des informations fournies ci-dessous.
- **Contexte** : Un référentiel de données métier — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-52 — Jeux de données de test — Cas limites et zones de risque [Jeux de données de test]

- **Rôle** : testeur QA.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le jeu de données de test fourni, et complète-le.
- **Contexte** : Un référentiel de données métier déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-53 — Jeux de données de test — Restitution en tableau structuré [Jeux de données de test]

- **Rôle** : testeur QA.
- **Tâche** : restitue le jeu de données de test sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Un référentiel de données métier, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-54 — Jeux de données de test — Audit et revue de conformité [Jeux de données de test]

- **Rôle** : testeur QA, en posture d'audit qualité.
- **Tâche** : relis le jeu de données de test fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Un référentiel de données métier, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-55 — Jeux de données de test — Adaptation à un autre contexte métier [Jeux de données de test]

- **Rôle** : testeur QA.
- **Tâche** : adapte ce modèle de le jeu de données de test (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Un référentiel de données métier existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-56 — Rapport de transmission des éléments de test — Génération initiale [Rapport de transmission des éléments de test]

- **Rôle** : assistant release management.
- **Tâche** : génère le rapport de transmission à partir des informations fournies ci-dessous.
- **Contexte** : Un changelog technique brut — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-57 — Rapport de transmission des éléments de test — Cas limites et zones de risque [Rapport de transmission des éléments de test]

- **Rôle** : assistant release management.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le rapport de transmission fourni, et complète-le.
- **Contexte** : Un changelog technique brut déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-58 — Rapport de transmission des éléments de test — Restitution en tableau structuré [Rapport de transmission des éléments de test]

- **Rôle** : assistant release management.
- **Tâche** : restitue le rapport de transmission sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Un changelog technique brut, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-59 — Rapport de transmission des éléments de test — Audit et revue de conformité [Rapport de transmission des éléments de test]

- **Rôle** : assistant release management, en posture d'audit qualité.
- **Tâche** : relis le rapport de transmission fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Un changelog technique brut, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-60 — Rapport de transmission des éléments de test — Adaptation à un autre contexte métier [Rapport de transmission des éléments de test]

- **Rôle** : assistant release management.
- **Tâche** : adapte ce modèle de le rapport de transmission (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Un changelog technique brut existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-61 — Journal de test / synthèse d'exécution — Génération initiale [Journal de test / synthèse d'exécution]

- **Rôle** : testeur QA.
- **Tâche** : génère le journal de test à partir des informations fournies ci-dessous.
- **Contexte** : Des résultats d'exécution bruts — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-62 — Journal de test / synthèse d'exécution — Cas limites et zones de risque [Journal de test / synthèse d'exécution]

- **Rôle** : testeur QA.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le journal de test fourni, et complète-le.
- **Contexte** : Des résultats d'exécution bruts déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-63 — Journal de test / synthèse d'exécution — Restitution en tableau structuré [Journal de test / synthèse d'exécution]

- **Rôle** : testeur QA.
- **Tâche** : restitue le journal de test sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Des résultats d'exécution bruts, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-64 — Journal de test / synthèse d'exécution — Audit et revue de conformité [Journal de test / synthèse d'exécution]

- **Rôle** : testeur QA, en posture d'audit qualité.
- **Tâche** : relis le journal de test fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Des résultats d'exécution bruts, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-65 — Journal de test / synthèse d'exécution — Adaptation à un autre contexte métier [Journal de test / synthèse d'exécution]

- **Rôle** : testeur QA.
- **Tâche** : adapte ce modèle de le journal de test (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Des résultats d'exécution bruts existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-66 — Rapport d'anomalie (bug report) — Génération initiale [Rapport d'anomalie (bug report)]

- **Rôle** : testeur QA.
- **Tâche** : génère le rapport d'anomalie à partir des informations fournies ci-dessous.
- **Contexte** : Une observation informelle de bug — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-67 — Rapport d'anomalie (bug report) — Cas limites et zones de risque [Rapport d'anomalie (bug report)]

- **Rôle** : testeur QA.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le rapport d'anomalie fourni, et complète-le.
- **Contexte** : Une observation informelle de bug déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-68 — Rapport d'anomalie (bug report) — Restitution en tableau structuré [Rapport d'anomalie (bug report)]

- **Rôle** : testeur QA.
- **Tâche** : restitue le rapport d'anomalie sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Une observation informelle de bug, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-69 — Rapport d'anomalie (bug report) — Audit et revue de conformité [Rapport d'anomalie (bug report)]

- **Rôle** : testeur QA, en posture d'audit qualité.
- **Tâche** : relis le rapport d'anomalie fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Une observation informelle de bug, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-70 — Rapport d'anomalie (bug report) — Adaptation à un autre contexte métier [Rapport d'anomalie (bug report)]

- **Rôle** : testeur QA.
- **Tâche** : adapte ce modèle de le rapport d'anomalie (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Une observation informelle de bug existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-71 — Rapport de statut intermédiaire — Génération initiale [Rapport de statut intermédiaire]

- **Rôle** : Test Manager.
- **Tâche** : génère le rapport de statut intermédiaire à partir des informations fournies ci-dessous.
- **Contexte** : Des données d'avancement de test — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-72 — Rapport de statut intermédiaire — Cas limites et zones de risque [Rapport de statut intermédiaire]

- **Rôle** : Test Manager.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le rapport de statut intermédiaire fourni, et complète-le.
- **Contexte** : Des données d'avancement de test déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-73 — Rapport de statut intermédiaire — Restitution en tableau structuré [Rapport de statut intermédiaire]

- **Rôle** : Test Manager.
- **Tâche** : restitue le rapport de statut intermédiaire sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Des données d'avancement de test, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-74 — Rapport de statut intermédiaire — Audit et revue de conformité [Rapport de statut intermédiaire]

- **Rôle** : Test Manager, en posture d'audit qualité.
- **Tâche** : relis le rapport de statut intermédiaire fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Des données d'avancement de test, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-75 — Rapport de statut intermédiaire — Adaptation à un autre contexte métier [Rapport de statut intermédiaire]

- **Rôle** : Test Manager.
- **Tâche** : adapte ce modèle de le rapport de statut intermédiaire (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Des données d'avancement de test existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-76 — Rapport de synthèse des tests (Test Summary) — Génération initiale [Rapport de synthèse des tests (Test Summary)]

- **Rôle** : Test Manager.
- **Tâche** : génère le rapport de synthèse des tests à partir des informations fournies ci-dessous.
- **Contexte** : Une RTM finale et un journal d'exécution — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-77 — Rapport de synthèse des tests (Test Summary) — Cas limites et zones de risque [Rapport de synthèse des tests (Test Summary)]

- **Rôle** : Test Manager.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le rapport de synthèse des tests fourni, et complète-le.
- **Contexte** : Une RTM finale et un journal d'exécution déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-78 — Rapport de synthèse des tests (Test Summary) — Restitution en tableau structuré [Rapport de synthèse des tests (Test Summary)]

- **Rôle** : Test Manager.
- **Tâche** : restitue le rapport de synthèse des tests sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Une RTM finale et un journal d'exécution, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-79 — Rapport de synthèse des tests (Test Summary) — Audit et revue de conformité [Rapport de synthèse des tests (Test Summary)]

- **Rôle** : Test Manager, en posture d'audit qualité.
- **Tâche** : relis le rapport de synthèse des tests fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Une RTM finale et un journal d'exécution, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-80 — Rapport de synthèse des tests (Test Summary) — Adaptation à un autre contexte métier [Rapport de synthèse des tests (Test Summary)]

- **Rôle** : Test Manager.
- **Tâche** : adapte ce modèle de le rapport de synthèse des tests (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Une RTM finale et un journal d'exécution existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-81 — Procès-verbal de recette (UAT) — Génération initiale [Procès-verbal de recette (UAT)]

- **Rôle** : analyste QA, support à la recette métier.
- **Tâche** : génère le script et le PV de recette à partir des informations fournies ci-dessous.
- **Contexte** : Des critères Gherkin validés — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-82 — Procès-verbal de recette (UAT) — Cas limites et zones de risque [Procès-verbal de recette (UAT)]

- **Rôle** : analyste QA, support à la recette métier.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le script et le PV de recette fourni, et complète-le.
- **Contexte** : Des critères Gherkin validés déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-83 — Procès-verbal de recette (UAT) — Restitution en tableau structuré [Procès-verbal de recette (UAT)]

- **Rôle** : analyste QA, support à la recette métier.
- **Tâche** : restitue le script et le PV de recette sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Des critères Gherkin validés, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-84 — Procès-verbal de recette (UAT) — Audit et revue de conformité [Procès-verbal de recette (UAT)]

- **Rôle** : analyste QA, support à la recette métier, en posture d'audit qualité.
- **Tâche** : relis le script et le PV de recette fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Des critères Gherkin validés, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-85 — Procès-verbal de recette (UAT) — Adaptation à un autre contexte métier [Procès-verbal de recette (UAT)]

- **Rôle** : analyste QA, support à la recette métier.
- **Tâche** : adapte ce modèle de le script et le PV de recette (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Des critères Gherkin validés existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-86 — Rapport de clôture / leçons apprises — Génération initiale [Rapport de clôture / leçons apprises]

- **Rôle** : Test Manager.
- **Tâche** : génère le rapport de clôture à partir des informations fournies ci-dessous.
- **Contexte** : Le bilan d'un cycle de test — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-87 — Rapport de clôture / leçons apprises — Cas limites et zones de risque [Rapport de clôture / leçons apprises]

- **Rôle** : Test Manager.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le rapport de clôture fourni, et complète-le.
- **Contexte** : Le bilan d'un cycle de test déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-88 — Rapport de clôture / leçons apprises — Restitution en tableau structuré [Rapport de clôture / leçons apprises]

- **Rôle** : Test Manager.
- **Tâche** : restitue le rapport de clôture sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Le bilan d'un cycle de test, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-89 — Rapport de clôture / leçons apprises — Audit et revue de conformité [Rapport de clôture / leçons apprises]

- **Rôle** : Test Manager, en posture d'audit qualité.
- **Tâche** : relis le rapport de clôture fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Le bilan d'un cycle de test, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-90 — Rapport de clôture / leçons apprises — Adaptation à un autre contexte métier [Rapport de clôture / leçons apprises]

- **Rôle** : Test Manager.
- **Tâche** : adapte ce modèle de le rapport de clôture (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Le bilan d'un cycle de test existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-91 — Release notes / dossier de livraison — Génération initiale [Release notes / dossier de livraison]

- **Rôle** : assistant release management.
- **Tâche** : génère les notes de version à partir des informations fournies ci-dessous.
- **Contexte** : Des tickets résolus et tests passés — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-92 — Release notes / dossier de livraison — Cas limites et zones de risque [Release notes / dossier de livraison]

- **Rôle** : assistant release management.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans les notes de version fourni, et complète-le.
- **Contexte** : Des tickets résolus et tests passés déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-93 — Release notes / dossier de livraison — Restitution en tableau structuré [Release notes / dossier de livraison]

- **Rôle** : assistant release management.
- **Tâche** : restitue les notes de version sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Des tickets résolus et tests passés, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-94 — Release notes / dossier de livraison — Audit et revue de conformité [Release notes / dossier de livraison]

- **Rôle** : assistant release management, en posture d'audit qualité.
- **Tâche** : relis les notes de version fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Des tickets résolus et tests passés, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-95 — Release notes / dossier de livraison — Adaptation à un autre contexte métier [Release notes / dossier de livraison]

- **Rôle** : assistant release management.
- **Tâche** : adapte ce modèle de les notes de version (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Des tickets résolus et tests passés existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

### FN-96 — Automatisation (scripts de test) — Génération initiale [Automatisation (scripts de test)]

- **Rôle** : ingénieur QA automatisation.
- **Tâche** : génère le script de test automatisé à partir des informations fournies ci-dessous.
- **Contexte** : Un parcours utilisateur ou une fonction à automatiser — à compléter avec les données réelles du projet.
- **Format** : structure standard du document, prête à relire et adapter.
- **Contraintes** : ne formule aucune hypothèse non vérifiable ; signale explicitement toute information manquante.

### FN-97 — Automatisation (scripts de test) — Cas limites et zones de risque [Automatisation (scripts de test)]

- **Rôle** : ingénieur QA automatisation.
- **Tâche** : identifie les cas limites, zones de risque ou angles morts non couverts dans le script de test automatisé fourni, et complète-le.
- **Contexte** : Un parcours utilisateur ou une fonction à automatiser déjà rédigé, à challenger.
- **Format** : liste des ajouts proposés, chacun justifié en une phrase.
- **Contraintes** : ne remets pas en cause ce qui est déjà correct ; concentre-toi uniquement sur les manques.

### FN-98 — Automatisation (scripts de test) — Restitution en tableau structuré [Automatisation (scripts de test)]

- **Rôle** : ingénieur QA automatisation.
- **Tâche** : restitue le script de test automatisé sous forme de tableau structuré exploitable par un outil de gestion de tests (export CSV ou Markdown).
- **Contexte** : Un parcours utilisateur ou une fonction à automatiser, déjà rédigé en texte libre.
- **Format** : tableau avec en-têtes explicites, une ligne par élément.
- **Contraintes** : conserve l'intégralité de l'information d'origine ; n'invente aucune colonne sans donnée correspondante.

### FN-99 — Automatisation (scripts de test) — Audit et revue de conformité [Automatisation (scripts de test)]

- **Rôle** : ingénieur QA automatisation, en posture d'audit qualité.
- **Tâche** : relis le script de test automatisé fourni et signale les incohérences, redondances ou écarts par rapport au format attendu.
- **Contexte** : Un parcours utilisateur ou une fonction à automatiser, à auditer avant validation finale.
- **Format** : liste numérotée des écarts, chacun avec sa correction proposée.
- **Contraintes** : reste factuel ; pas de jugement de valeur sur le style, uniquement sur la conformité et la cohérence.

### FN-100 — Automatisation (scripts de test) — Adaptation à un autre contexte métier [Automatisation (scripts de test)]

- **Rôle** : ingénieur QA automatisation.
- **Tâche** : adapte ce modèle de le script de test automatisé (initialement conçu pour le module Panier) à un nouveau contexte métier précisé par l'utilisateur.
- **Contexte** : Un parcours utilisateur ou une fonction à automatiser existant, à transposer (ex : module paiement, module compte client, autre secteur).
- **Format** : même structure que l'original, contenu entièrement réécrit pour le nouveau contexte.
- **Contraintes** : ne conserve aucun détail spécifique à l'exemple Panier sauf s'il reste pertinent.

## Templates de Context Engineering (CE-01 à CE-35)

### CE-01 — Rôle métier précis [Rôle / Persona]

- **Template** : Rôle : {rôle précis, ex. "Test Manager certifié ISTQB Advanced"}.
- **Pourquoi ça marche** : Un rôle précis cadre le niveau de langage, les priorités et les réflexes attendus dans la réponse.

### CE-02 — Rôle + posture [Rôle / Persona]

- **Template** : Rôle : {rôle}, en posture {d'audit / de pédagogue / de challenge critique}.
- **Pourquoi ça marche** : La posture oriente le ton : un audit cherche les failles, une pédagogie explique, un challenge questionne les choix.

### CE-03 — Rôle + niveau d'expérience [Rôle / Persona]

- **Template** : Rôle : {rôle}, avec {N années} d'expérience sur des projets {type de projet}.
- **Pourquoi ça marche** : Préciser l'expérience évite les réponses trop génériques ou trop débutantes pour le besoin réel.

### CE-04 — Spécification brute intégrée [Fourniture de spécifications]

- **Template** : Contexte : voici la spécification exacte à respecter : {coller le texte}.
- **Pourquoi ça marche** : Donner le texte source évite à l'IA de deviner ou de réinventer une spécification approximative.

### CE-05 — Référence à un document externe [Fourniture de spécifications]

- **Template** : Contexte : ce travail doit respecter le document {nom du document}, dont voici les points clés : {résumé}.
- **Pourquoi ça marche** : Resumer plutôt que copier intégralement permet de rester dans la limite de contexte tout en gardant l'essentiel.

### CE-06 — Contraintes techniques explicites [Fourniture de spécifications]

- **Template** : Contexte : le système utilise {techno/langage/version} ; toute solution doit être compatible.
- **Pourquoi ça marche** : Sans cette précision, l'IA génère parfois du code ou des formats incompatibles avec la stack réelle.

### CE-07 — Règle métier formulée en langage naturel [Règles métier]

- **Template** : Règle métier : {énoncé de la règle, ex. "une remise ne s'applique jamais sur les frais de port"}.
- **Pourquoi ça marche** : Les règles métier ne sont jamais déductibles du code seul ; elles doivent être explicitées.

### CE-08 — Règle métier sous forme de table de décision [Règles métier]

- **Template** : Règle métier (table) : {condition 1} → {résultat 1} ; {condition 2} → {résultat 2}.
- **Pourquoi ça marche** : Le format tabulaire réduit l'ambiguïté pour les règles à embranchements multiples.

### CE-09 — Exceptions à la règle générale [Règles métier]

- **Template** : Règle métier : {règle générale}. Exception : {cas particulier où elle ne s'applique pas}.
- **Pourquoi ça marche** : Nommer explicitement l'exception évite que l'IA généralise la règle à tort.

### CE-10 — Un exemple complet entrée/sortie [Few-shot (exemples)]

- **Template** : Exemple : pour l'entrée {X}, la sortie attendue est {Y}.
- **Pourquoi ça marche** : Un seul exemple bien choisi cadre le format mieux qu'une longue description abstraite.

### CE-11 — Deux exemples contrastés [Few-shot (exemples)]

- **Template** : Exemple 1 (cas simple) : {...}. Exemple 2 (cas limite) : {...}.
- **Pourquoi ça marche** : Contraster un cas simple et un cas limite montre l'étendue du comportement attendu, pas seulement le cas facile.

### CE-12 — Contre-exemple explicite [Few-shot (exemples)]

- **Template** : Ne fais surtout pas comme dans cet exemple raté : {exemple à éviter}, parce que {raison}.
- **Pourquoi ça marche** : Montrer ce qu'il ne faut pas faire est parfois plus efficace que de multiplier les bons exemples.

### CE-13 — Format structuré strict [Format de sortie]

- **Template** : Format : {tableau / JSON / Gherkin / code exécutable}, aucun texte hors de cette structure.
- **Pourquoi ça marche** : Un format strict permet d'automatiser l'intégration de la réponse dans un autre outil sans retraitement manuel.

### CE-14 — Gabarit à remplir [Format de sortie]

- **Template** : Format : remplis exactement ce gabarit, section par section : {coller le gabarit vide}.
- **Pourquoi ça marche** : Fournir le gabarit vide garantit que toutes les sections obligatoires seront couvertes.

### CE-15 — Longueur contrainte [Format de sortie]

- **Template** : Format : {N} éléments maximum, chacun en une phrase.
- **Pourquoi ça marche** : Contraindre la longueur évite les réponses diluées qui noient l'information utile.

### CE-16 — Interdiction d'inventer [Garde-fous]

- **Template** : Contrainte : si une information manque, indique-le explicitement plutôt que de l'inventer.
- **Pourquoi ça marche** : C'est le garde-fou le plus important en contexte de test : une donnée inventée peut invalider toute une suite de tests.

### CE-17 — Limites du périmètre [Garde-fous]

- **Template** : Contrainte : ne traite que {périmètre précis} ; ignore tout ce qui sort de ce périmètre.
- **Pourquoi ça marche** : Borner le périmètre évite les réponses qui dérivent vers des sujets adjacents non demandés.

### CE-18 — Obligation de relecture humaine [Garde-fous]

- **Template** : Contrainte : cette sortie doit être relue et validée par un humain avant exécution ou diffusion.
- **Pourquoi ça marche** : Rappeler la relecture dans le prompt lui-même renforce le réflexe, même si la vérification reste humaine et hors-prompt.

### CE-19 — Référentiel de nommage [Référentiels]

- **Template** : Référentiel : utilise la nomenclature suivante pour les identifiants : {règle de nommage, ex. CT-XX}.
- **Pourquoi ça marche** : Un identifiant cohérent avec l'existant permet l'intégration directe dans la documentation du projet.

### CE-20 — Référentiel de sévérité/priorité [Référentiels]

- **Template** : Référentiel : utilise cette échelle de sévérité : {Bloquante / Majeure / Mineure / Cosmétique}.
- **Pourquoi ça marche** : Sans échelle partagée, deux testeurs (ou deux sessions IA) classifient différemment la même anomalie.

### CE-21 — Référentiel de glossaire métier [Référentiels]

- **Template** : Référentiel : voici les termes métier à utiliser strictement tels quels : {glossaire}.
- **Pourquoi ça marche** : Le vocabulaire métier mal employé peut faire perdre confiance au lecteur métier dans tout le document.

### CE-22 — Contexte d'architecture [Contexte projet]

- **Template** : Contexte projet : l'application est structurée ainsi : {schéma résumé de l'architecture}.
- **Pourquoi ça marche** : Situer la fonctionnalité dans l'architecture évite les tests d'intégration mal ciblés.

### CE-23 — Contexte d'équipe et de méthodologie [Contexte projet]

- **Template** : Contexte projet : équipe de {N} personnes, méthodologie {Agile/cycle en V}, cycle de {durée}.
- **Pourquoi ça marche** : Le contexte organisationnel influence la granularité réaliste des livrables demandés.

### CE-24 — Contexte de build / version [Contexte projet]

- **Template** : Contexte projet : ce travail concerne le build {identifiant}, qui inclut les changements suivants : {liste}.
- **Pourquoi ça marche** : Lier explicitement au build évite la confusion entre versions lors du suivi des anomalies.

### CE-25 — Glossaire technique minimal [Glossaire]

- **Template** : Glossaire : {terme technique} signifie {définition courte}.
- **Pourquoi ça marche** : Définir les acronymes du projet (RTM, UAT, CT-XX) évite les mauvaises interprétations dans les sorties.

### CE-26 — Glossaire métier minimal [Glossaire]

- **Template** : Glossaire métier : {terme métier} désigne {définition courte, propre à l'organisation}.
- **Pourquoi ça marche** : Un même mot (ex. "client") peut désigner des entités différentes selon les organisations.

### CE-27 — Découpage en étapes explicites [Décomposition]

- **Template** : Tâche découpée : Étape 1 — {...}. Étape 2 — {...}. Étape 3 — {...}.
- **Pourquoi ça marche** : Décomposer une tâche complexe en étapes réduit les oublis et facilite la relecture partielle.

### CE-28 — Une sous-tâche par appel [Décomposition]

- **Template** : Contrainte : traite uniquement {sous-tâche unique} dans cette réponse ; les autres sous-tâches feront l'objet d'appels séparés.
- **Pourquoi ça marche** : Limiter le périmètre par appel améliore la qualité de chaque réponse individuelle.

### CE-29 — Plan avant exécution [Décomposition]

- **Template** : Tâche : propose d'abord un plan en 3-5 points, sans le détailler ; j'approuverai avant que tu développes.
- **Pourquoi ça marche** : Valider le plan avant le détail évite de devoir tout refaire si l'angle d'approche ne convient pas.

### CE-30 — Relecture demandée explicitement [Auto-vérification]

- **Template** : Contrainte : avant de répondre, vérifie que chaque élément produit est cohérent avec le contexte fourni.
- **Pourquoi ça marche** : Demander une auto-relecture réduit (sans l'éliminer) le risque d'incohérence interne dans une longue réponse.

### CE-31 — Vérification croisée avec une référence [Auto-vérification]

- **Template** : Contrainte : vérifie que ta réponse est cohérente avec {document de référence fourni} avant de la formuler.
- **Pourquoi ça marche** : Ancrer la vérification sur un document précis est plus fiable qu'une vérification "dans l'absolu".

### CE-32 — Jeu de données d'exemple fourni [Données de référence]

- **Template** : Données de référence : voici un extrait représentatif des données réelles : {extrait anonymisé}.
- **Pourquoi ça marche** : Des données réelles (anonymisées) produisent des cas de test bien plus pertinents que des données inventées.

### CE-33 — Plage de valeurs autorisées [Données de référence]

- **Template** : Données de référence : les valeurs valides pour {champ} sont : {liste ou plage}.
- **Pourquoi ça marche** : Sans cette borne, l'IA peut générer des cas de test sur des valeurs qui n'existeront jamais en production.

### CE-34 — Demander une estimation de confiance [Gestion de l'incertitude]

- **Template** : Contrainte : pour chaque élément généré, indique ton niveau de confiance (élevé/moyen/faible).
- **Pourquoi ça marche** : Cela aide le testeur humain à prioriser sa relecture sur les éléments les moins fiables.

### CE-35 — Lister les hypothèses faites [Gestion de l'incertitude]

- **Template** : Contrainte : termine ta réponse par la liste des hypothèses que tu as dû faire faute d'information.
- **Pourquoi ça marche** : Expliciter les hypothèses transforme un risque caché en point de vérification visible.
