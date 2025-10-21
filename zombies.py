import random

def attaquer_camp(survivants, ressources, difficulte="normal"):
    """Gère l'attaque des zombies, avec une difficulté variable."""
    nombre_zombies = 50 if difficulte == "max" else random.randint(5, 20)
    print(f"{nombre_zombies} zombies attaquent le camp.")
    
    if ressources["munitions"] >= nombre_zombies:
        ressources["munitions"] -= nombre_zombies
        return

    for s in survivants:
        if random.randint(0, 100) < s["precision"]:
            nombre_zombies -= 1
        else:
            s["sante"] -= random.randint(10, 30)
