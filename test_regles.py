from regles import evaluer_votes


def test_CA_02_1_strict_tour_1_unanimite():
    # Vérifie le cas de la règle stricte.
    votes = [5, 5, 5]
    regle = "strict"
    tour = 1
    statut, valeur = evaluer_votes(votes, regle, tour)
    assert statut == "validé"
    assert valeur == 5


def test_CA_02_4_strict_tour_1_divergence():
    votes = [5, 5, 8]
    regle = "strict"
    tour = 1
    statut, valeur = evaluer_votes(votes, regle, tour)
    assert statut == "revote"
    assert valeur is None


def test_CA_02_3_moyenne_tour_1_unanimite_obligatoire():
    # Vérifie que le tour 1 exige toujours l'unanimité même si la règle choisie est la moyenne.
    votes = [3, 5, 8]
    regle = "moyenne"
    tour = 1
    statut, valeur = evaluer_votes(votes, regle, tour)
    assert statut == "revote"
    assert valeur is None


def test_CA_02_2_moyenne_tour_2_arrondi_proche():
    votes = [3, 5, 8]
    regle = "moyenne"
    tour = 2
    statut, valeur = evaluer_votes(votes, regle, tour)
    assert statut == "validé"
    assert valeur == 5


def test_CA_02_6_moyenne_tour_2_equidistance_superieure():
    # Vérifie le choix de la carte supérieure (5) quand la moyenne (4) est pile entre 3 et 5.
    votes = [1, 3, 8]
    regle = "moyenne"
    tour = 2
    statut, valeur = evaluer_votes(votes, regle, tour)
    assert statut == "validé"
    assert valeur == 5


def test_CA_02_7_moyenne_tour_2_carte_incertitude():
    votes = [5, 5, "?"]
    regle = "moyenne"
    tour = 2
    statut, valeur = evaluer_votes(votes, regle, tour)
    assert statut == "revote"
    assert valeur is None
