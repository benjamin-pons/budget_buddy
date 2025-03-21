import customtkinter
import re
from textbox import TextBox
from connexion_module import ConnexionModule
from home import HomeFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Budget Buddy")
        self.geometry("700x600")
        self.grid_columnconfigure((0,2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Starts Main Menu
        self.main_menu = MainMenu(self)
        self.main_menu.grid(row=0, column=1, sticky="ew")


    def show_main_menu(self):
        """Opens main menu"""
        if hasattr(self, "signup_frame"):
            self.signup_frame.grid_forget()
        if hasattr(self, "login_frame"):
            self.login_frame.grid_forget()
        if hasattr(self, "home_frame"):
            self.home_frame.grid_forget()

        self.main_menu.grid(row=0, column=1, sticky="ew")

    def show_signup(self):
        """Opens sign up menu"""
        self.main_menu.grid_forget()
        self.signup_frame = SignUpFrame(self)
        self.signup_frame.grid(row=0, column=1, sticky="ew")

    def show_login(self):
        """Opens login menu"""
        self.main_menu.grid_forget()
        self.login_frame = LoginFrame(self)
        self.login_frame.grid(row=0, column=1, sticky="ew")
    
    def show_home(self, user_id):
        """Open home after connection"""
        self.main_menu.grid_forget()
        if hasattr(self, "signup_frame"):
            self.signup_frame.grid_forget()
        if hasattr(self, "login_frame"):
            self.login_frame.grid_forget()

        self.home_frame = HomeFrame(self, user_id)
        self.home_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)


class MainMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.label = customtkinter.CTkLabel(self, text="Budget Buddy", font=("Double struck", 30), fg_color="gray30", corner_radius=6)
        self.label.grid(row=0, column=0, pady=20, padx=30, ipadx=10, ipady=10, sticky="n")

        self.signup_button = customtkinter.CTkButton(self, text="Créer un compte", command=master.show_signup)
        self.signup_button.grid(row=1, column=0, pady=20, padx=20, sticky="ew")

        self.login_button = customtkinter.CTkButton(self, text="Se connecter", command=master.show_login)
        self.login_button.grid(row=2, column=0, pady=20, padx=20, sticky="ew")


class SignUpFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(self, text="S'inscrire", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.textbox_name = TextBox(self, "Nom :", 2)
        self.textbox_fname = TextBox(self, "Prénom :", 4)
        self.textbox_email = TextBox(self, "Email :", 6)
        self.textbox_password = TextBox(self, "Mot de passe :", 8)

        self.button = customtkinter.CTkButton(self, text="Valider", command=self.button_sign_up)
        self.button.grid(row=10, column=0, padx=20, pady=20)

        self.error_message = customtkinter.CTkLabel(self, text="", text_color="red", font=("Arial", 14))
        self.error_message.grid(row=11, column=0, pady=5)

        self.back_button = customtkinter.CTkButton(self, text="Retour au menu", command=master.show_main_menu)
        self.back_button.grid(row=12, column=0, padx=20, pady=20, sticky="ew")

    def button_sign_up(self):
        result = [
            self.textbox_name.get_text(),
            self.textbox_fname.get_text(),
            self.textbox_email.get_text(),
            self.textbox_password.get_text(),
        ]
        
        # If password doesn't meet requirments
        if not self.is_valid_password(result[3]):
            self.error_message.configure(text="Mot de passe invalide")
            self.after(5000, self.clear_error_message)
        else:
            conn_module = ConnexionModule()
            conn_module.create_user(result[2], result[3], result[0], result[1])

    def is_valid_password(self, password):
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{10,}$"
        return bool(re.match(regex, password))
    
    def clear_error_message(self):
        self.error_message.configure(text="")


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.title = customtkinter.CTkLabel(self, text="Se connecter", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.textbox_email = TextBox(self, "Email :", 2)
        self.textbox_password = TextBox(self, "Mot de passe :", 4)

        self.button = customtkinter.CTkButton(self, text="Se connecter", command=self.button_login)
        self.button.grid(row=6, column=0, padx=20, pady=20)

        self.back_button = customtkinter.CTkButton(self, text="Retour au menu", command=master.show_main_menu)
        self.back_button.grid(row=12, column=0, padx=20, pady=20, sticky="ew")

        self.error_message = customtkinter.CTkLabel(self, text="", text_color="red", font=("Arial", 14))
        self.error_message.grid(row=11, column=0, pady=5)
    
    def button_login(self) :
        result = [
            self.textbox_email.get_text(),
            self.textbox_password.get_text()
        ]

        conn_module = ConnexionModule()        
        if conn_module.check_user(result[0], result[1]) :
            print("ACCES AUTORISE")
            self.master.show_home(conn_module.get_user_id(result[0]))
        else :
            print("ACCES REFUSE")
            self.error_message.configure(text="Mot de passe/Email invalide")
            self.after(5000, self.clear_error_message)
    
    def clear_error_message(self):
        self.error_message.configure(text="")

if __name__ == "__main__":
    app = App()
    app.mainloop()
