import customtkinter as ctk

# Configuration de l'apparence
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Thèmes: "blue" (default), "green", "dark-blue"

# Création de la fenêtre principale
app = ctk.CTk()
app.title("Budget Buddy")
app.geometry("400x300")  # Taille de la fenêtre

# Fonctions pour les boutons 
def creer_compte():
    print("Créer un compte")

def se_connecter():
    print("Se connecter")

# Titre de l'application
titre = ctk.CTkLabel(app, text="Budget Buddy", font=("Arial", 24, "bold"))
titre.pack(pady=20)

# Bouton "Se créer un compte"
bouton_creer_compte = ctk.CTkButton(app, text="Se créer un compte", command=creer_compte, fg_color="#4CAF50", hover_color="#45a049")
bouton_creer_compte.pack(pady=10)

# Bouton "Se connecter"
bouton_se_connecter = ctk.CTkButton(app, text="Se connecter", command=se_connecter, fg_color="#2196F3", hover_color="#1976D2")
bouton_se_connecter.pack(pady=10)

# Lancement de l'application
app.mainloop()