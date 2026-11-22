CARTES_FIBONACCI = [0, 1, 2, 3, 5, 8, 13, 20, 40, 100]


def _regle_strict(votes: list) -> tuple:
    # En mode strict, il faut une unanimité parfaite (déjà vérifiée en amont)
    return ("revote", None)


def _regle_moyenne(votes: list) -> tuple:
    # Si un joueur a voté '?' ou 'café', impossible de calculer une moyenne numérique
    if any(not isinstance(v, (int, float)) for v in votes):
        return ("revote", None)

    moyenne = sum(votes) / len(votes)

    # Trouve la carte Fibonacci la plus proche ; en cas d'égalité exacte, prend la supérieure
    meilleure_carte = min(
        CARTES_FIBONACCI,
        key=lambda carte: (round(abs(carte - moyenne), 6), -carte)
    )
    return ("validé", meilleure_carte)


REGLES_DISPONIBLES = {
    "strict": _regle_strict,
    "moyenne": _regle_moyenne,
}


def evaluer_votes(votes: list, regle: str, tour: int) -> tuple:
    """
    Évalue une liste de votes selon la règle ("strict" ou "moyenne") et le tour (1 ou 2).
    """
    if not votes:
        return ("revote", None)

    # Cas unanime (tous les joueurs ont voté la même carte)
    if len(set(votes)) == 1:
        carte_unique = votes[0]
        if carte_unique == "café":
            return ("pause", "café")
        if carte_unique == "?":
            return ("revote", None)
        return ("validé", carte_unique)

    # Le tour 1 impose toujours l'unanimité quelle que soit la règle choisie
    if tour == 1:
        return ("revote", None)

    # Au tour 2+, on applique la stratégie correspondant à la règle choisie
    if regle not in REGLES_DISPONIBLES:
        raise ValueError(f"Règle inconnue : {regle}")

    return REGLES_DISPONIBLES[regle](votes)
