from account import Account
from transaction import Transaction
import customtkinter
import mysql.connector
from connexion_module import ConnexionModule
from datetime import datetime

class TransactionFrame(customtkinter.CTkFrame):
    def __init__(self, master, account_id, user_id, return_callback):
        super().__init__(master)
        self.master = master
        self.account_id = account_id
        self.user_id = user_id
        self.return_callback = return_callback

        self.transaction_obj = Transaction()
        self.transaction_data = self.load_transactions()

        self.setup_ui()
        self.display_transactions()

    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)

        self.return_button = customtkinter.CTkButton(self, text="Retour", command=self.return_home)
        self.return_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.title_label = customtkinter.CTkLabel(self, text="Historique des Transactions", font=("Arial", 20, "bold"))
        self.title_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.new_transaction_button = customtkinter.CTkButton(self, text="Nouvelle Transaction", command=self.show_new_transaction_menu)
        self.new_transaction_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.transactions_frame = customtkinter.CTkFrame(self)
        self.transactions_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    def show_new_transaction_menu(self):
        self.grid_forget()
        self.new_transaction_menu = NewTransactionFrame(self.master, self, self.account_id)
        self.new_transaction_menu.grid(row=0, column=0, sticky="nsew")

    def load_transactions(self):
        transaction_data = self.transaction_obj.get_all_transactions(self.account_id)
        return transaction_data

    def display_transactions(self):
        for widget in self.transactions_frame.winfo_children():
            widget.destroy()  # Nettoyer l'affichage précédent

        for index, transaction in enumerate(self.transaction_data):
            self.create_transaction_widget(transaction, index)
            
    def return_home(self) :
        home_frame = self.master
        if hasattr(home_frame, 'return_to_home'):
            home_frame.return_to_home()
        


    def create_transaction_widget(self, transaction, index):
        transaction_frame = customtkinter.CTkFrame(self.transactions_frame)
        transaction_frame.grid(row=index, column=0, padx=10, pady=5, sticky="w")

        date_label = customtkinter.CTkLabel(transaction_frame, text=f"Date : {transaction['date']}", font=("Arial", 14))
        date_label.grid(row=0, column=0, padx=5, pady=2, sticky="w")

        description_label = customtkinter.CTkLabel(transaction_frame, text=f"{transaction['description']}", font=("Arial", 12))
        description_label.grid(row=1, column=0, columnspan=2, padx=5, pady=2, sticky="w")

        amount_color = "green" if transaction["amount"] >= 0 else "red"
        amount_text = f"+{transaction['amount']} €" if transaction["amount"] >= 0 else f"{transaction['amount']} €"
        amount_label = customtkinter.CTkLabel(transaction_frame, text=f"Montant : {amount_text}", font=("Arial", 14, "bold"), text_color=amount_color)
        amount_label.grid(row=0, column=1, padx=5, pady=2, sticky="w")

        separator = customtkinter.CTkFrame(self.transactions_frame, height=1, fg_color="gray")
        separator.grid(row=index + 1, column=0, padx=5, pady=5, sticky="ew")

class NewTransactionFrame(customtkinter.CTkFrame):
    def __init__(self, master, previous_frame, account_id):
        super().__init__(master)
        self.master = master
        self.previous_frame = previous_frame
        self.account_id = account_id
        self.setup_ui()
        self.transaction_obj = Transaction()

    def setup_ui(self):
        """New transaction menu"""
        self.grid_columnconfigure(0, weight=1)

        self.title_label = customtkinter.CTkLabel(self, text="Nouvelle Transaction", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.amount_entry = customtkinter.CTkEntry(self, placeholder_text="Montant (€)")
        self.amount_entry.grid(row=1, column=0, padx=10, pady=5)

        self.description_entry = customtkinter.CTkEntry(self, placeholder_text="Description")
        self.description_entry.grid(row=2, column=0, padx=10, pady=5)

        self.submit_button = customtkinter.CTkButton(self, text="Ajouter", command=self.add_transaction)
        self.submit_button.grid(row=3, column=0, padx=5, pady=5)

        self.cancel_button = customtkinter.CTkButton(self, text="Annuler", command=self.return_to_transaction_frame)
        self.cancel_button.grid(row=4, column=0, padx=5, pady=5)

    def add_transaction(self):
        amount = float(self.amount_entry.get())
        print(amount)
        description = self.description_entry.get()

        date_now = datetime.now()
        date = date_now.strftime("%Y-%m-%d")

        if amount and description:
            if amount > 0 :
                self.transaction_obj.deposit(description, amount, date, self.account_id)
            elif amount < 0 :
                self.transaction_obj.withdrawal(description, amount, date, self.account_id)
            self.return_to_transaction_frame()
            

    def return_to_transaction_frame(self):
        self.grid_forget()  # Cache ce menu
        self.previous_frame.grid(row=0, column=0, sticky="nsew")  # Réaffiche TransactionFrame
