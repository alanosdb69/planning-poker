CARTES_FIBONACCI = [0, 1, 2, 3, 5, 8, 13, 20, 40, 100]


def _regle_strict(votes: list) -> tuple:
    return ("revote", None)


def _regle_moyenne(votes: list) -> tuple:
    if any(not isinstance(v, (int, float)) for v in votes):
        return ("revote", None)

    moyenne = sum(votes) / len(votes)
    meilleure_carte = min(
        CARTES_FIBONACCI,
        key=lambda carte: (round(abs(carte - moyenne), 6), -carte)
    )
    return ("validé", meilleure_carte)


# Ajouter une nouvelle règle consiste uniquement à ajouter une fonction et une entrée dans REGLES_DISPONIBLES sans modifier les règles existantes.
REGLES_DISPONIBLES = {
    "strict": _regle_strict,
    "moyenne": _regle_moyenne,
}


def evaluer_votes(votes: list, regle: str, tour: int) -> tuple:
    if not votes:
        return ("revote", None)

    if len(set(votes)) == 1:
        carte_unique = votes[0]
        if carte_unique == "café":
            return ("pause", "café")
        if carte_unique == "?":
            return ("revote", None)
        return ("validé", carte_unique)

    if tour == 1:
        return ("revote", None)

    if regle not in REGLES_DISPONIBLES:
        raise ValueError(f"Règle inconnue : {regle}")

    return REGLES_DISPONIBLES[regle](votes)