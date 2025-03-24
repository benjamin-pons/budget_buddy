import customtkinter
import mysql.connector
from textbox import TextBox, SmallTextBox
from account import Account
from connexion_module import ConnexionModule

class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master, user_id):
        super().__init__(master)

        conn_module = ConnexionModule()
        self.user_id = user_id
        self.user_info = conn_module.get_user_info(user_id)

        self.grid_columnconfigure(0, weight=1)  
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_rowconfigure(2, weight=2)

        welcome_text = "Bienvenue " + self.user_info["fname"] + " sur votre espace personnel !"
        self.label = customtkinter.CTkLabel(self, text=welcome_text, font = ("Arial", 25))
        self.label.grid(row=0, column=0, pady=20, padx=20, sticky="n")

        self.account_select = AccountSelect(self, user_id, )
        self.account_select.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        self.logout_button = customtkinter.CTkButton(self, text="Déconnexion", command=master.show_main_menu)
        self.logout_button.grid(row=2, column=0 , pady=10, padx=20, ipadx=50)
    
    def refresh_accounts_list(self) :
        self.account_select.refresh_accounts()

        


class AccountSelect(customtkinter.CTkScrollableFrame):
    def __init__(self, master, user_id) :
        super().__init__(master, orientation="horizontal")
        self.grid_columnconfigure(0, weight=1)

        self.user_id = user_id
        self.account_obj = Account()

        self.refresh_accounts()

    def refresh_accounts(self):
        for widget in self.winfo_children():
            widget.destroy()

        new_account = CreateAccountFrame(self, self.user_id, self.refresh_accounts)
        new_account.grid_propagate(False)
        new_account.grid(row=0, column=0, padx=10, pady=(10, 20))

        account_list = self.account_obj.get_all_accounts_info(self.user_id)
        print("BOOOOOOOOOOOOOOOO")
        print(len(account_list))

        for index, account in enumerate(account_list):
            account_frame = AccountFrame(self, account["name_account"], account["balance"])
            account_frame.grid_propagate(False)
            account_frame.grid(row=0, column=index + 1, padx=10)


class AccountFrame(customtkinter.CTkFrame) :
    def __init__(self, master, name, balance) :
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        text_balance = str(balance) + " €"
        account_name = customtkinter.CTkLabel(self, text=name, font = ("Arial", 30))
        account_name.grid(row=0, column=0)

        account_balance = customtkinter.CTkLabel(self, text=text_balance, font = ("Arial", 30))
        account_balance.grid(row=1, column=0)
    
    


class CreateAccountFrame(customtkinter.CTkFrame) :
    def __init__(self, master, user_id, refresh_callback):
        super().__init__(master)
        self.user_id = user_id
        self.refresh_callback = refresh_callback
        self.create_initial_ui()
        
    

    def create_initial_ui(self):
        """Displays initial interface with create account button"""
        for widget in self.winfo_children():
            widget.destroy()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.new_account_button = customtkinter.CTkButton(self, text="Créer un compte", command=self.create_account)
        self.new_account_button.grid(row=0, column=0, pady=10, padx=10)

    def create_account(self) :
        for widget in self.winfo_children():
            widget.destroy()
        
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.new_account_textbox = SmallTextBox(self, "Nom", 1)

        account_name = self.new_account_textbox.get_text()

        confirm_button = customtkinter.CTkButton(self, text="Confirmer", command=self.create_account_db)
        confirm_button.grid(row=2, column=0, padx=5, pady=10)

        cancel_button = customtkinter.CTkButton(self, text="Annuler", command=self.cancel)
        cancel_button.grid(row=2, column=1, padx=5, pady=10)

    def create_account_db(self) :
        account_name = self.new_account_textbox.get_text().strip()

        if not account_name:
            return

        account_obj = Account()
        account_obj.create_account(account_name, self.user_id)

        self.refresh_callback()

        self.create_initial_ui()
        

    def cancel(self) :
        self.create_initial_ui()
