def creer_survivant(nom):
    """Crée un survivant avec des statistiques de base."""
    return {"nom": nom, "sante": 100, "moral": 100, "fatigue": 0, "force": 5, "precision": 70}



def entrainer_survivants(survivants):
    """Augmente la force et la précision des survivants."""
    print("\nLes survivants s'entraînent pour améliorer leurs compétences.")
    for s in survivants:
        s["force"] += 1
        s["precision"] = min(100, s["precision"] + 2)
    print("L'entraînement a renforcé les survivants.")

def recuperer_survivants(survivants):
    """Récupère la fatigue et améliore la santé des survivants."""
    print("\nLes survivants se reposent et récupèrent un peu de fatigue et de santé.")
    for s in survivants:
        # Réduction de la fatigue (la fatigue ne doit pas dépasser 100)
        if s["fatigue"] > 0:
            s["fatigue"] = max(0, s["fatigue"] - 20)
        
        # Récupération de santé (la santé ne doit pas dépasser 100)
        if s["sante"] < 100:
            s["sante"] = min(100, s["sante"] + 10)
    
    print("Les survivants ont récupéré un peu de fatigue et de santé.")
