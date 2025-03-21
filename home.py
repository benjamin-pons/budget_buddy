import customtkinter
import mysql.connector
from connexion_module import ConnexionModule

class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master, user_id):
        super().__init__(master)

        conn_module = ConnexionModule()
        self.user_info = conn_module.get_user_info(user_id)

        self.grid_columnconfigure(0, weight=1)  
        self.grid_rowconfigure((0, 1, 2), weight=1)

        welcome_text = "Bienvenue " + self.user_info["fname"] + " sur votre espace personnel !"
        self.label = customtkinter.CTkLabel(self, text=welcome_text, font = ("Arial", 25))
        self.label.grid(row=0, column=0, pady=20, padx=20, sticky="n")

        self.logout_button = customtkinter.CTkButton(self, text="Déconnexion", command=master.show_main_menu)
        self.logout_button.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        self.grid_rowconfigure(2, weight=2)

        

        

        
