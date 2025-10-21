import unittest
import random

# Fonction pour générer un événement aléatoire (par exemple, une tempête ou une attaque de pillards)
def evenement_aleatoire(ressources):
    """Simule un événement aléatoire qui affecte les ressources."""
    chance_tempete = 0.1
    chance_pillards = 0.2
    chance = random.random()

    if chance < chance_tempete:
        # Tempête : perte de nourriture et d'eau
        ressources["eau"] = max(0, ressources["eau"] - 5)
        ressources["nourriture"] = max(0, ressources["nourriture"] - 5)
        print("Une tempête a ravagé le camp ! Perte d'eau et de nourriture.")
    
    elif chance < chance_tempete + chance_pillards:
        # Attaque de pillards : perte de munitions et de bois
        ressources["munitions"] = max(0, ressources["munitions"] - 3)
        ressources["bois"] = max(0, ressources["bois"] - 3)
        print("Des pillards ont attaqué le camp ! Perte de munitions et de bois.")

# Test unitaire simplifié
class TestEvenements(unittest.TestCase):

    def test_evenement_aleatoire(self):
        # Création des ressources initiales
        ressources = {"eau": 20, "nourriture": 20, "munitions": 10, "bois": 10}

        # On simule un événement aléatoire
        evenement_aleatoire(ressources)

        # Vérification si les ressources ont diminué de façon réaliste (en fonction de l'événement)
        self.assertTrue(ressources["eau"] <= 20, "L'eau ne devrait pas être plus que 20 après l'événement.")
        self.assertTrue(ressources["nourriture"] <= 20, "La nourriture ne devrait pas être plus que 20 après l'événement.")
        self.assertTrue(ressources["munitions"] <= 10, "Les munitions ne devraient pas être plus que 10 après l'événement.")
        self.assertTrue(ressources["bois"] <= 10, "Le bois ne devrait pas être plus que 10 après l'événement.")

if __name__ == "__main__":
    unittest.main()
