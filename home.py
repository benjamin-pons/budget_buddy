import customtkinter

class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)  
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.label = customtkinter.CTkLabel(self, text="Bienvenue sur votre espace personnel !")
        self.label.grid(row=0, column=0, pady=20, padx=20, sticky="n")

        self.logout_button = customtkinter.CTkButton(self, text="Déconnexion", command=master.show_main_menu)
        self.logout_button.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        self.grid_rowconfigure(2, weight=2)