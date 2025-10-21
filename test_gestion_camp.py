import unittest
from gestion_camp import consommer_ressources, fin_de_jour
from config import CONSOMMATION_EAU, CONSOMMATION_NOURRITURE

def test_consommer_ressources():
    """Teste la fonction consommer_ressources."""
    survivants = [{"nom": "Alex", "sante": 100}]
    ressources = {"eau": 10, "nourriture": 10}
    
    consommer_ressources(ressources, survivants)
    assert ressources["eau"] == 9, f"Erreur : eau devrait être 9, trouvé {ressources['eau']}"
    assert ressources["nourriture"] == 9, f"Erreur : nourriture devrait être 9, trouvé {ressources['nourriture']}"

def test_fin_de_jour():
    """Teste la fonction fin_de_jour."""
    survivants = [{"nom": "Alex", "sante": 100, "fatigue": 0}]
    ressources = {"eau": 10, "nourriture": 10}
    
    fin_de_jour(survivants, ressources)
    assert survivants[0]["fatigue"] > 0, f"Erreur : la fatigue devrait être augmentée"

def run_tests():
    """
    Execute les tests définis.
    """
test_functions = [test_consommer_ressources, test_fin_de_jour]
for test in test_functions:
    try:
        test()
        print(f" {test.__name__} : OK")
    except AssertionError as e:
        print(f" {test.__name__} : Echec")
        print(f" {e}")

if __name__ == "__main__":
    run_tests()
