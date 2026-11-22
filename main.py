import json
import os
from getpass import getpass
from regles import evaluer_votes

CARTES_VALIDES = {"0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "?", "café"}


def creer_partie(joueurs: list[str]) -> dict:
    if len(joueurs) < 2:
        raise ValueError("Il faut au moins 2 joueurs.")
    return {
        "joueurs": joueurs,
        "index_courant": 0
    }


def charger_backlog(chemin_fichier: str) -> dict:
    if not os.path.exists(chemin_fichier):
        raise FileNotFoundError(f"Le fichier '{chemin_fichier}' n'existe pas.")

    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "fonctionnalites" not in data or not data["fonctionnalites"]:
        raise ValueError("Le backlog ne contient aucune fonctionnalité valide.")

    return data


def obtenir_premiere_fonctionnalite(backlog: dict) -> dict:
    return backlog["fonctionnalites"][0]


def saisir_joueurs() -> list[str]:
    while True:
        try:
            nb = int(input("Nombre de joueurs (minimum 2) : "))
            if nb >= 2:
                break
            print("Erreur : entrez au moins 2 joueurs.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.")

    joueurs = []
    for i in range(nb):
        nom = input(f"Pseudo du joueur {i + 1} : ").strip()
        while not nom:
            nom = input(f"Le pseudo ne peut être vide. Pseudo {i + 1} : ").strip()
        joueurs.append(nom)
    return joueurs


def choisir_regle() -> str:
    while True:
        regle = input("Choisissez la règle de validation (strict / moyenne) : ").strip().lower()
        if regle in ("strict", "moyenne"):
            return regle
        print("Erreur : choisissez 'strict' ou 'moyenne'.")


def saisir_vote_cache(joueur: str):
    while True:
        choix = getpass(f"Vote caché de {joueur} (cartes : 0, 1, 2, 3, 5, 8, 13, 20, 40, 100, ?, café) : ").strip().lower()
        if choix in CARTES_VALIDES:
            return int(choix) if choix.isdigit() else choix
        print("Carte invalide, réessayez.")


def jouer_fonctionnalite(fonctionnalite: dict, joueurs: list[str], regle: str):
    print(f"\n=== Estimation de [{fonctionnalite['id']}] {fonctionnalite['titre']} ===")
    tour = 1
    while True:
        print(f"\n--- Tour {tour} (règle : {regle}) ---")
        votes = [saisir_vote_cache(joueur) for joueur in joueurs]

        print("\nRévélation des votes :")
        for joueur, vote in zip(joueurs, votes):
            print(f" - {joueur} : {vote}")

        statut, valeur = evaluer_votes(votes, regle, tour)

        if statut == "validé":
            print(f"\n-> Fonctionnalité VALIDÉE avec {valeur} points !")
            fonctionnalite["estimation"] = valeur
            break
        elif statut == "pause":
            print("\n-> Unanimité 'café' : pause demandée !")
            break
        else:
            print("\n-> Pas d'accord : nouveau tour de vote !")
            tour += 1


def lancer_application():
    print(" Démarrage Planning Poker ")
    joueurs = saisir_joueurs()
    partie = creer_partie(joueurs)
    print(f"\nPartie initialisée avec {len(partie['joueurs'])} joueurs : {', '.join(partie['joueurs'])}.")

    regle = choisir_regle()

    chemin_json = "exemples/backlog.json"
    print(f"\nChargement du backlog depuis '{chemin_json}'...")
    try:
        backlog = charger_backlog(chemin_json)
        premiere = obtenir_premiere_fonctionnalite(backlog)
        print(f"Projet : {backlog.get('projet', 'Sans nom')}")
        jouer_fonctionnalite(premiere, partie["joueurs"], regle)
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")


if __name__ == "__main__":
    lancer_application()
