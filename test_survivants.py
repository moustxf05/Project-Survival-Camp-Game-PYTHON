import unittest

# Fonction de création d'un survivant
def creer_survivant(nom):
    return {"nom": nom, "sante": 100, "moral": 100, "fatigue": 0, "force": 5, "precision": 70}

# Fonction de repos pour un survivant
def reposer_survivant(survivant):
    survivant["fatigue"] = max(0, survivant["fatigue"] - 20)
    survivant["moral"] = min(100, survivant["moral"] + 5)
    if survivant["sante"] < 100:
        soin = min(10, 100 - survivant["sante"])
        survivant["sante"] += soin
        print(f"{survivant['nom']} récupère {soin} points de santé grâce au repos.")

# Test unitaire simple
class TestSurvivant(unittest.TestCase):

    def test_creer_survivant(self):
        survivant = creer_survivant("John")
        self.assertEqual(survivant["nom"], "John")
        self.assertEqual(survivant["sante"], 100)
        self.assertEqual(survivant["moral"], 100)
        self.assertEqual(survivant["fatigue"], 0)
        self.assertEqual(survivant["force"], 5)
        self.assertEqual(survivant["precision"], 70)

    def test_reposer_survivant(self):
        survivant = creer_survivant("Jane")
        survivant["fatigue"] = 50  # Ajoutons un peu de fatigue
        survivant["sante"] = 90  # La santé de départ n'est pas pleine

        reposer_survivant(survivant)

        # Vérification des effets du repos
        self.assertEqual(survivant["fatigue"], 30)  # Fatigue réduite de 20
        self.assertEqual(survivant["moral"], 100)  # Moral augmente de 5 (max 100)
        self.assertEqual(survivant["sante"], 100)  # Santé augmentée (max 10)

if __name__ == "__main__":
    unittest.main()
