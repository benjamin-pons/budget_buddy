import customtkinter
import re
from textbox import TextBox
from connexion_module import ConnexionModule

class App(customtkinter.CTk) :
    def __init__(self):
        super().__init__()
        self.title("Budget Buddy")
        self.geometry("700x600")
        self.grid_columnconfigure((0,2), weight=1)
        self.grid_rowconfigure((0,2), weight=1)


        self.display_sign_in()
    
    def display_sign_in(self) :
        self.textboxframe = TextBoxFrame(self)
        self.textboxframe.grid(row=1, column=1, padx=10, rowspan=1, columnspan=1, sticky="nsew")
    

    # If password doesn't meet requirments
    def display_error(self) :
        self.error_message = customtkinter.CTkLabel(
                self.textboxframe,
                text="Mot de passe invalide",
                text_color="red",
                font=("Arial", 16)
            )
        self.error_message.grid(row=9, column=0, padx=20, pady=10, sticky="ew")
        print("MDP invalide")
        self.after(5000, self.delete_error)
    
    def delete_error(self) :
        self.error_message.configure(text="")
        

class TextBoxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.title = customtkinter.CTkLabel(self, text="S'inscrire", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.textbox_name = TextBox(self, "Nom :", "Valider", 2)
        self.textbox_fname = TextBox(self, "Prénom :", "Valider", 4)
        self.textbox_email = TextBox(self, "Email :", "Valider", 6)
        self.textbox_password = TextBox(self, "Mot de passe :", "Valider", 8)

        self.button = customtkinter.CTkButton(self, text="Valider", command=self.button_callback)
        self.button.grid(row = 10, column = 0, padx=20, pady=20)
    
    def button_callback(self):
        result = []
        result.append(self.textbox_name.get_text())
        result.append(self.textbox_fname.get_text())
        result.append(self.textbox_email.get_text())
        result.append(self.textbox_password.get_text())

        print(result)

        if not self.is_valid_password(result[3]) :
            app.display_sign_in()
            app.display_error()
        
        else :
            conn_module = ConnexionModule()
            conn_module.create_user(result[2], result[3], result[0], result[1])

            

    
    def is_valid_password(self, password) :
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{10,}$"
        if re.match(regex, password) :
            return True
        else :
            return False
        

if __name__ == "__main__":
    app = App()
    app.mainloop()