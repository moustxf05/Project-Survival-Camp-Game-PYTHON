import random
from config import CHANCE_PILLARDS, CHANCE_TEMPETE, CHANCE_MALADIE, CHANCE_OBJET_RARE

def evenement_aleatoire(survivants, ressources):
    """Déclenche un événement aléatoire qui impacte le camp."""
    evenement = random.choice(["rien", "ravitaillement", "tempête", "pillards", "maladie", "objet_rare"])

    if evenement == "rien":
        return
    elif evenement == "ravitaillement":
        ressources["nourriture"] += 5
        ressources["eau"] += 3
    elif evenement == "tempête" and random.random() < CHANCE_TEMPETE:
        ressources["bois"] = max(0, ressources["bois"] - 3)
    elif evenement == "pillards" and random.random() < CHANCE_PILLARDS:
        ressources["munitions"] = max(0, ressources["munitions"] - 3)
    elif evenement == "maladie" and random.random() < CHANCE_MALADIE:
        random.choice(survivants)["sante"] -= 10
    elif evenement == "objet_rare" and random.random() < CHANCE_OBJET_RARE:
        ressources["outils"] += 1
