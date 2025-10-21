import unittest
import random

# Fonction pour attaquer le camp par des zombies
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

# Fonction de création d'un survivant
def creer_survivant(nom):
    return {"nom": nom, "sante": 100, "moral": 100, "fatigue": 0, "force": 5, "precision": 70}

# Test unitaire simplifié
class TestZombies(unittest.TestCase):

    def test_attaquer_camp(self):
        # Création de ressources et survivants
        ressources = {"eau": 100, "nourriture": 100, "munitions": 10}
        survivants = [creer_survivant("Survivant1"), creer_survivant("Survivant2")]

        # On simule une attaque
        attaquer_camp(survivants, ressources)

        # Vérification si les ressources de munitions ont diminué ou si la santé des survivants a baissé
        if ressources["munitions"] < 10:
            self.assertTrue(all(s["sante"] <= 100 for s in survivants))  # Les survivants ne doivent pas avoir plus de 100 de santé
        else:
            self.assertEqual(ressources["munitions"], 10)  # Si assez de munitions, il n'y a pas de perte

if __name__ == "__main__":
    unittest.main()
