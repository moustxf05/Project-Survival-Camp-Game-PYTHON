import unittest
from expeditions import partir_en_expedition, combattre_pillards
from config import CHANCE_PILLARDS

def test_partir_en_expedition():
    """Teste la fonction partir_en_expedition."""
    survivants = [{"nom": "Alex", "sante": 100, "precision": 70}]
    ressources = {"eau": 10, "nourriture": 10, "munitions": 10, "bois": 5}
    
    # Avant expédition
    ressources_initiales = ressources.copy()
    partir_en_expedition(ressources, survivants)
    assert ressources["eau"] > ressources_initiales["eau"], f"Erreur : l'eau devrait être augmentée"
    
def test_combattre_pillards():
    """Teste la fonction combattre_pillards."""
    survivants = [{"nom": "Alex", "sante": 100, "precision": 70}]
    ressources = {"munitions": 10, "nourriture": 10}
    
    # Avant combat
    ressources_initiales = ressources.copy()
    combattre_pillards(survivants, ressources)
    assert ressources["munitions"] == ressources_initiales["munitions"] - 2, f"Erreur : les munitions devraient être réduites"

def run_tests():
    """
    Execute les tests définis.
    """
test_functions = [test_partir_en_expedition, test_combattre_pillards]
for test in test_functions:
    try:
        test()
        print(f" {test.__name__} : OK")
    except AssertionError as e:
        print(f" {test.__name__} : Echec")
        print(f" {e}")

if __name__ == "__main__":
    run_tests()
