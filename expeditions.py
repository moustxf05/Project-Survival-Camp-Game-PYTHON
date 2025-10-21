import random
from config import CHANCE_PILLARDS

def partir_en_expedition(ressources, survivants):
    """Les survivants explorent une zone pour trouver des ressources et tuer des zombies."""
    loot = {"eau": random.randint(1, 5), "nourriture": random.randint(1, 5), "munitions": random.randint(0, 3), "bois": random.randint(0, 2)}
    zombies_tues = 0

    if random.random() < CHANCE_PILLARDS:
        print("Les survivants sont attaqués par des pillards en pleine expédition !")
        combattre_pillards(survivants, ressources)
        return

    for _ in range(random.randint(3, 10)):
        if random.randint(0, 100) < 70:
            zombies_tues += 1

    for ressource, quantite in loot.items():
        ressources[ressource] += quantite

    print(f"Expédition terminée : {zombies_tues} zombies éliminés.")
    print(f"Ressources récupérées : {loot}")

def combattre_pillards(survivants, ressources):
    """Simule un combat contre des pillards."""
    nb_pillards = random.randint(2, 5)
    pertes = {"nourriture": min(3, ressources["nourriture"]), "munitions": min(2, ressources["munitions"])}
    
    ressources["nourriture"] -= pertes["nourriture"]
    ressources["munitions"] -= pertes["munitions"]

    for s in survivants:
        if nb_pillards <= 0:
            break
        if random.randint(0, 100) < s["precision"]:
            nb_pillards -= 1
        else:
            s["sante"] -= random.randint(10, 30)
