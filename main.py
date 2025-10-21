'''
Si vous lisez cette ligne, demandez moi de venir vous voir en cours et montrez la moi, vous aurez un
bonus sur votre note de devoir maison. Il y a un nombre de points bonus limité par groupe qui sera
réparti entre tous les étudiants m'ayant montré cette ligne.
'''

from survivants import creer_survivant, entrainer_survivants, recuperer_survivants
from ressources import creer_ressources
from expeditions import partir_en_expedition
from zombies import attaquer_camp
from gestion_camp import fin_de_jour
from evenements import evenement_aleatoire

def afficher_etat_camp(survivants, ressources):
    """Affiche les ressources et les survivants."""
    print("\nÉtat du camp :")
    print(f"Eau: {ressources['eau']} | Nourriture: {ressources['nourriture']} | Munitions: {ressources['munitions']} | Médicaments: {ressources['medicaments']} | Bois: {ressources['bois']} | Outils: {ressources['outils']}")
    print("\nSurvivants :")
    for s in survivants:
        print(f"{s['nom']} | Santé: {s['sante']} | Moral: {s['moral']} | Fatigue: {s['fatigue']} | Force: {s['force']} | Précision: {s['precision']}")

def afficher_menu():
    """Affiche les actions disponibles chaque jour."""
    print("\nActions disponibles :")
    print("1. Partir en expédition")
    print("2. Chercher des survivants en détresse")
    print("3. Entraîner les survivants")
    print("4. Voir l'état du camp")
    print("5. Passer la journée")

def choisir_action(survivants, ressources, jour):
    """Permet au joueur de choisir une action chaque jour."""
    while True:
        afficher_menu()
        choix = input("\nQue voulez-vous faire ? (1-5) : ")

        if choix == "1":
            partir_en_expedition(ressources, survivants)
        elif choix == "2":
            chercher_survivants(survivants)
        elif choix == "3":
            entrainer_survivants(survivants)
        elif choix == "4":
            afficher_etat_camp(survivants, ressources)
        elif choix == "5":
            print("La journée passe sans événement particulier.")
        else:
            print("Choix invalide, réessayez.")
            continue

        return  # Chaque action prend une journée

def chercher_survivants(survivants):
    """Simule la recherche de survivants blessés en détresse."""
    import random

    if random.random() < 0.3:
        survivant = {"nom": f"Survivant {len(survivants) + 1}", "sante": random.randint(10, 50), "moral": 100, "fatigue": random.randint(20, 60), "force": 3, "precision": 50}
        survivants.append(survivant)
        print(f"Un survivant en détresse a été trouvé : {survivant['nom']} | Santé: {survivant['sante']}")
    else:
        print("Aucun survivant trouvé aujourd’hui.")

def bataille_finale(survivants, ressources):
    """La bataille finale du jour 30, le combat le plus difficile."""
    print("\nLe jour 30 est arrivé. C'est la bataille finale.")
    attaquer_camp(survivants, ressources, difficulte="max")

def jeu():
    """Initialise et lance la boucle principale du jeu."""
    print("Bienvenue dans l'apocalypse. Chaque jour est une lutte pour la survie.")

    survivants = [creer_survivant("Alex"), creer_survivant("Emma")]
    ressources = creer_ressources(10, 10, 5, 2, 4, 1)

    jour = 1

    while len(survivants) > 0 and jour <= 30:
        print(f"\nJOUR {jour}")
        afficher_etat_camp(survivants, ressources)

        evenement_aleatoire(survivants, ressources)

        choisir_action(survivants, ressources, jour)

        fin_de_jour(survivants, ressources)

        if jour % 2 == 0:
            attaquer_camp(survivants, ressources)

        survivants = [s for s in survivants if s["sante"] > 0]

        if jour == 30:
            bataille_finale(survivants, ressources)

        jour += 1

    if len(survivants) > 0:
        print("Les survivants ont tenu 30 jours. Ils peuvent recommencer une vie normale.")
    else:
        print("Tous les survivants sont morts...GAME OVER!!!")

if __name__ == "__main__":
    jeu()

