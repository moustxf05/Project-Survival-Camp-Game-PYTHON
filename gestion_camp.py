from config import CONSOMMATION_EAU, CONSOMMATION_NOURRITURE

def consommer_ressources(ressources, survivants):
    """Chaque survivant consomme des ressources."""
    ressources["eau"] = max(0, ressources["eau"] - len(survivants) * CONSOMMATION_EAU)
    ressources["nourriture"] = max(0, ressources["nourriture"] - len(survivants) * CONSOMMATION_NOURRITURE)

def fin_de_jour(survivants, ressources):
    """Gère la fin de journée."""
    consommer_ressources(ressources, survivants)
    for s in survivants:
        s["fatigue"] += 10
        if s["fatigue"] >= 100:
            s["sante"] -= 10
