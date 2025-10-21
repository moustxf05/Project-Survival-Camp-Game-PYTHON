import unittest
from config import (
    SANTE_INITIALE,
    CONSOMMATION_EAU,
    CONSOMMATION_NOURRITURE,
    PERTE_SANTE_FAIM,
    PERTE_SANTE_SOIF,
    CHANCE_NOUVEAU_SURVIVANT,
    CHANCE_PILLARDS,
    CHANCE_TEMPETE,
    CHANCE_MALADIE,
    CHANCE_OBJET_RARE
)

def test_config():
    """
    Teste les constantes du module config.
    """
    assert SANTE_INITIALE == 100, f"Erreur : SANTE_INITIALE doit être 100, trouvé {SANTE_INITIALE}"
    assert CONSOMMATION_EAU == 1, f"Erreur : CONSOMMATION_EAU doit être 1, trouvé {CONSOMMATION_EAU}"
    assert CONSOMMATION_NOURRITURE == 1, f"Erreur : CONSOMMATION_NOURRITURE doit être 1, trouvé {CONSOMMATION_NOURRITURE}"
    assert PERTE_SANTE_FAIM == 15, f"Erreur : PERTE_SANTE_FAIM doit être 15, trouvé {PERTE_SANTE_FAIM}"
    assert PERTE_SANTE_SOIF == 20, f"Erreur : PERTE_SANTE_SOIF doit être 20, trouvé {PERTE_SANTE_SOIF}"
    assert CHANCE_NOUVEAU_SURVIVANT == 0.5, f"Erreur : CHANCE_NOUVEAU_SURVIVANT doit être 0.5, trouvé {CHANCE_NOUVEAU_SURVIVANT}"
    assert CHANCE_PILLARDS == 0.2, f"Erreur : CHANCE_PILLARDS doit être 0.2, trouvé {CHANCE_PILLARDS}"
    assert CHANCE_TEMPETE == 0.1, f"Erreur : CHANCE_TEMPETE doit être 0.1, trouvé {CHANCE_TEMPETE}"
    assert CHANCE_MALADIE == 0.15, f"Erreur : CHANCE_MALADIE doit être 0.15, trouvé {CHANCE_MALADIE}"
    assert CHANCE_OBJET_RARE == 0.3, f"Erreur : CHANCE_OBJET_RARE doit être 0.3, trouvé {CHANCE_OBJET_RARE}"

def run_tests():
    """
    Execute les tests définis.
    """
test_functions = [test_config]
for test in test_functions:
    try:
        test()
        print(f" {test.__name__} : OK")
    except AssertionError as e:
        print(f" {test.__name__} : Echec")
        print(f" {e}")

if __name__ == "__main__":
    run_tests()
