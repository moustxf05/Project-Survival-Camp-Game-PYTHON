def creer_ressources(eau, nourriture, munitions, medicaments, bois, outils):
    """Crée et initialise les ressources du camp."""
    return {
        "eau": eau,
        "nourriture": nourriture,
        "munitions": munitions,
        "medicaments": medicaments,
        "bois": bois,
        "outils": outils
    }

def consommer_ressources(ressources, survivants):
    """Chaque survivant consomme une unité d'eau et de nourriture par jour."""
    ressources["eau"] = max(0, ressources["eau"] - len(survivants))
    ressources["nourriture"] = max(0, ressources["nourriture"] - len(survivants))

def verifier_etat_ressources(ressources):
    """Affiche l'état des ressources du camp."""
    print("\nÉtat des ressources :")
    for ressource, quantite in ressources.items():
        print(f"{ressource.capitalize()} : {quantite}")

def recuperer_ressources(ressources, loot):
    """Ajoute les ressources récupérées en expédition."""
    for ressource, quantite in loot.items():
        ressources[ressource] += quantite
    print(f"Ressources ajoutées : {loot}")

def utiliser_medicament(survivants, ressources):
    """Utilise un médicament pour soigner un survivant blessé."""
    blesses = [s for s in survivants if s["sante"] < 100]

    if ressources["medicaments"] <= 0:
        print("Aucun médicament disponible.")
        return

    if not blesses:
        print("Aucun survivant n'a besoin de soins.")
        return

    survivant = blesses[0]
    soins = min(30, 100 - survivant["sante"])
    survivant["sante"] += soins
    ressources["medicaments"] -= 1

    print(f"{survivant['nom']} a été soigné et récupère {soins} points de santé.")
