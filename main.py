import json
import os

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

def lancer_application():
    print(" Démarrage Planning Poker ")
    joueurs = saisir_joueurs()
    partie = creer_partie(joueurs)
    print(f"\nPartie initialisée avec {len(partie['joueurs'])} joueurs : {', '.join(partie['joueurs'])}.")
    chemin_json = "exemples/backlog.json"
    print(f"\nChargement du backlog depuis '{chemin_json}'...")
    try:
        backlog = charger_backlog(chemin_json)
        premiere = obtenir_premiere_fonctionnalite(backlog)
        print(f"Projet : {backlog.get('projet', 'Sans nom')}")
        print(f"-> Première fonctionnalité à estimer : [{premiere['id']}] {premiere['titre']}")
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")

if __name__ == "__main__":
    lancer_application()
