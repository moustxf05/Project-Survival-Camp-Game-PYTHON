import unittest
from ressources import creer_ressources

class TestRessources(unittest.TestCase):

    def test_creer_ressources(self):
        """Teste la fonction creer_ressources pour vérifier si elle retourne les bonnes ressources."""
        # Appel de la fonction avec des paramètres de test
        ressources = creer_ressources(10, 20, 30, 40, 50, 60)

        # Vérification des valeurs des ressources
        self.assertEqual(ressources["eau"], 10)
        self.assertEqual(ressources["nourriture"], 20)
        self.assertEqual(ressources["munitions"], 30)
        self.assertEqual(ressources["medicaments"], 40)
        self.assertEqual(ressources["bois"], 50)
        self.assertEqual(ressources["outils"], 60)

if __name__ == "__main__":
    unittest.main()
