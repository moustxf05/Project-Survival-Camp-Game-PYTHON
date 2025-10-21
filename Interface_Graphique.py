import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Ajout pour gérer les images
import random

# --- CONFIGURATION ---
SANTE_INITIALE = 100
CONSOMMATION_EAU = 1
CONSOMMATION_NOURRITURE = 1
PERTE_SANTE_FAIM = 15
PERTE_SANTE_SOIF = 20
CHANCE_NOUVEAU_SURVIVANT = 0.3

# --- CLASSES ET FONCTIONS DU JEU ---

def creer_survivant(nom):
    return {"nom": nom, "sante": SANTE_INITIALE, "moral": 100, "fatigue": 0, "force": 5, "precision": 70}

def creer_ressources(eau, nourriture, munitions, medicaments, bois, outils):
    return {"eau": eau, "nourriture": nourriture, "munitions": munitions, "medicaments": medicaments, "bois": bois, "outils": outils}

def consommer_ressources():
    ressources["eau"] = max(0, ressources["eau"] - len(survivants) * CONSOMMATION_EAU)
    ressources["nourriture"] = max(0, ressources["nourriture"] - len(survivants) * CONSOMMATION_NOURRITURE)

def fin_de_jour():
    consommer_ressources()
    for s in survivants:
        s["fatigue"] += 10
        if ressources["nourriture"] == 0:
            s["sante"] -= PERTE_SANTE_FAIM
        if ressources["eau"] == 0:
            s["sante"] -= PERTE_SANTE_SOIF
        if s["fatigue"] >= 100:
            s["sante"] -= 10

def partir_en_expedition():
    loot = {"eau": random.randint(1, 5), "nourriture": random.randint(1, 5), "munitions": random.randint(0, 3), "bois": random.randint(0, 2)}
    for ressource, quantite in loot.items():
        ressources[ressource] += quantite
    afficher_message(f"Expédition : +{loot}")
    avancer_jour()

def chercher_survivants():
    if random.random() < CHANCE_NOUVEAU_SURVIVANT:
        new_survivant = creer_survivant(f"Survivant {len(survivants)+1}")
        survivants.append(new_survivant)
        afficher_message(f"Nouveau survivant trouvé : {new_survivant['nom']}")
    else:
        afficher_message("Aucun survivant trouvé aujourd'hui.")
    avancer_jour()

def entrainer_survivants():
    for s in survivants:
        s["force"] += 1
        s["precision"] = min(100, s["precision"] + 2)
    afficher_message("Les survivants se sont entraînés.")
    avancer_jour()

def passer_journee():
    afficher_message("La journée passe sans événement particulier.")
    avancer_jour()

def avancer_jour():
    global jour
    jour += 1
    fin_de_jour()
    maj_affichage()
    verifier_survivants()
    if jour > 30:
        messagebox.showinfo("Victoire", "Les survivants ont tenu 30 jours !")
        root.destroy()

def afficher_etat_camp():
    maj_affichage()
    afficher_message("État du camp mis à jour.")

def afficher_message(msg):
    message_text.configure(state="normal")
    message_text.insert(tk.END, msg + "\n")
    message_text.configure(state="disabled")
    message_text.see(tk.END)

def maj_affichage():
    jour_var.set(f"Jour {jour}")
    ressources_var.set(f"Eau: {ressources['eau']} | Nourriture: {ressources['nourriture']} | Munitions: {ressources['munitions']} | Médicaments: {ressources['medicaments']} | Bois: {ressources['bois']} | Outils: {ressources['outils']}")
    survivants_list.delete(*survivants_list.get_children())
    for s in survivants:
        survivants_list.insert("", tk.END, values=(s['nom'], s['sante'], s['moral'], s['fatigue'], s['force'], s['precision']))

def verifier_survivants():
    global survivants
    survivants = [s for s in survivants if s["sante"] > 0]
    if not survivants:
        messagebox.showinfo("Fin du Jeu", "Tous les survivants sont morts... Game Over.")
        root.destroy()

# --- INITIALISATION ---

jour = 1
survivants = [creer_survivant("Alex"), creer_survivant("Emma")]
ressources = creer_ressources(10, 10, 5, 2, 4, 1)

# --- INTERFACE TKINTER ---

root = tk.Tk()
root.title("Camp de Survie")

# Frame principale divisée en 3 colonnes
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)

frame_gauche = ttk.Frame(main_frame, width=200)
frame_gauche.pack(side="left", fill="y")

frame_centre = ttk.Frame(main_frame)
frame_centre.pack(side="left", fill="both", expand=True)

frame_droite = ttk.Frame(main_frame, width=300)
frame_droite.pack(side="right", fill="y")

# --- Centre : Le Jeu ---

frame_jour = ttk.Frame(frame_centre, padding=10)
frame_jour.pack()
jour_var = tk.StringVar()
jour_label = ttk.Label(frame_jour, textvariable=jour_var, font=("Arial", 16))
jour_label.pack()

frame_ressources = ttk.Frame(frame_centre, padding=10)
frame_ressources.pack()
ressources_var = tk.StringVar()
ressources_label = ttk.Label(frame_ressources, textvariable=ressources_var)
ressources_label.pack()

frame_survivants = ttk.Frame(frame_centre, padding=10)
frame_survivants.pack()
survivants_list = ttk.Treeview(frame_survivants, columns=("Nom", "Santé", "Moral", "Fatigue", "Force", "Précision"), show="headings", height=6)
for col in ("Nom", "Santé", "Moral", "Fatigue", "Force", "Précision"):
    survivants_list.heading(col, text=col)
    survivants_list.column(col, width=100)
survivants_list.pack()

frame_boutons = ttk.Frame(frame_centre, padding=10)
frame_boutons.pack()

ttk.Button(frame_boutons, text="Expédition", command=partir_en_expedition).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame_boutons, text="Chercher Survivants", command=chercher_survivants).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_boutons, text="Entraîner Survivants", command=entrainer_survivants).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(frame_boutons, text="Passer Journée", command=passer_journee).grid(row=1, column=1, padx=5, pady=5)
ttk.Button(frame_boutons, text="Afficher État", command=afficher_etat_camp).grid(row=2, column=0, columnspan=2, pady=5)
ttk.Button(frame_boutons, text="Quitter", command=root.destroy).grid(row=3, column=0, columnspan=2, pady=5)

frame_messages = ttk.Frame(frame_centre, padding=10)
frame_messages.pack()
message_text = tk.Text(frame_messages, height=10, width=70, state="disabled", background="#f0f0f0")
message_text.pack()

# --- Droite : Image Zombie ---

try:
    image_origine = Image.open("Zombie.png")
    largeur, hauteur = image_origine.size
    rapport = hauteur / largeur

    nouvelle_largeur = 300
    nouvelle_hauteur = int(nouvelle_largeur * rapport)

    image_redimensionnee = image_origine.resize((nouvelle_largeur, nouvelle_hauteur))
    zombie_image = ImageTk.PhotoImage(image_redimensionnee)

    image_label = ttk.Label(frame_droite, image=zombie_image)
    image_label.pack(fill="both", expand=True)
except Exception as e:
    print(f"Erreur lors du chargement de l'image : {e}")

# --- Lancer l'affichage initial ---

maj_affichage()

# --- Démarrer l'interface graphique ---

root.mainloop()
