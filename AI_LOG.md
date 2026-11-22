# AI_LOG.md : journal d'usage de l'IA

## Outils utilisés

| Outil | Modèle | Mode |
|---|---|---|
| Gemini | Web | Chat |

Fichier d'instructions pour agent versionné : non

## Entrées

### 2026-11-07 : Bloc C - Squelette de code Sprint 1 (US-01, US-03)
- **Demande** : Écriture du script initial en Python (`main.py`) pour la saisie des participants et la lecture du backlog JSON, en séparant la logique métier de l'interface console.
- **Résultat** : Modifié
- **Ce que nous avons vérifié** : Bonne lecture de `exemples/backlog.json` et exécution en ligne de commande avec `python main.py`.
- **Ce que nous avons changé ou rejeté** : Retrait du moteur de calcul des votes (strict/moyenne) afin de le développer lors de la séance 2.

### 2026-11-22 : Bloc B - Workflow d'intégration continue (CI GitHub Actions)
- **Demande** : Rédaction d'un workflow GitHub Actions (`.github/workflows/ci.yml`) déclenché sur `push` et `pull_request` vers `main` pour exécuter `pytest` avec Python 3.12.
- **Résultat** : Modifié
- **Ce que nous avons vérifié** : Le passage au rouge initial de la CI sur les 6 tests de `test_regles.py` (`NotImplementedError`), ainsi que les permissions `contents: read` et le blocage d'échec par défaut de `pytest`.
- **Ce que nous avons changé ou rejeté** : Suppression de l'ancien fichier `test_main.py` qui faisait échouer la collecte des tests, et rédaction personnelle des commentaires explicatifs sur chaque bloc du fichier YAML.

### 2026-11-22 : Bloc C - Implémentation du moteur de règles et intégration (`regles.py`, `main.py`)
- **Demande** : Implémentation de la fonction `evaluer_votes` dans `regles.py` selon nos 6 tests unitaires (sans les modifier) avec une architecture extensible, et branchement du vote caché (`getpass`) et de la révélation dans `main.py`.
- **Résultat** : Modifié
- **Ce que nous avons vérifié** : Passage au vert de l'ensemble des 6 tests unitaires dans la Pull Request #1, gestion du premier tour à l'unanimité et protection contre les listes de votes vides.
- **Ce que nous avons changé ou rejeté** : Découpage des règles dans des fonctions dédiées reliées par un dictionnaire `REGLES_DISPONIBLES` afin de pouvoir ajouter une nouvelle règle sans modifier les règles existantes.

## Bilan (à compléter en séance 4, 3 lignes)
- Nombre d'entrées et de propositions rejetées ou corrigées :
- Tâches où l'IA a fait gagner du temps :
- Tâches où l'IA a fait perdre du temps :
