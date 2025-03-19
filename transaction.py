import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

class Transaction():
    def __init__(self):
        self.db_host = os.getenv("DB_HOST")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_database = os.getenv("DB_DATABASE")

        try:
            self.conn = mysql.connector.connect(
                host=self.db_host,
                user=self.db_user,
                password=self.db_password,
                database=self.db_database
            )
            self.cursor = self.conn.cursor()  
        except mysql.connector.Error as err:
            print(f"Erreur de connexion à la base de données : {err}")
            self.conn = None

    def deposit(self, description, amount, date, account_id):
        # Loads current balance in 'old_balance'
        query = "SELECT balance FROM account WHERE id_account = %s"
        self.cursor.execute(query, (account_id,))
        old_balance = self.cursor.fetchone()

        try:

            new_balance = old_balance[0] + amount

            # Update new balance in account
            query = "UPDATE account SET balance = %s WHERE id_account = %s"
            values = (new_balance, account_id)
            self.cursor.execute(query, values)
            self.conn.commit()  

            # Create new transaction
            query = "INSERT INTO transaction (description, amount, date, type, account_id) VALUES (%s, %s, %s, %s, %s)"
            values = (description, amount, date, 'deposit', account_id)
            self.cursor.execute(query, values)
            self.conn.commit()

        except mysql.connector.Error as err:
            print(f"Erreur lors de la transaction : {err}")

    def withdrawal(self, description, amount, date, account_id):
        query = "SELECT balance FROM account WHERE id_account = %s"
        self.cursor.execute(query, (account_id,))
        old_balance = self.cursor.fetchone()

        try:

            new_balance = old_balance[0] - amount

            # Update new balance in account
            query = "UPDATE account SET balance = %s WHERE id_account = %s"
            values = (new_balance, account_id)
            self.cursor.execute(query, values)
            self.conn.commit()  

            # Create new transaction
            query = "INSERT INTO transaction (description, amount, date, type, account_id) VALUES (%s, %s, %s, %s, %s)"
            values = (description, amount, date, 'withdrawal', account_id)
            self.cursor.execute(query, values)
            self.conn.commit()

        except mysql.connector.Error as err:
            print(f"Erreur lors de la transaction : {err}")

    def transfer(self, description, amount, date, sender_account, recipient_account):
        self.withdrawal(description, amount, date, sender_account)
        self.deposit(description, amount, date, recipient_account)



    
transaction = Transaction()
# transaction.deposit("France Travail", 552, "2025-04-03", 1)
# transaction.withdrawal("France Travail", 500, "2025-04-04", 1)
transaction.transfer("Velodrome", 200, "2025-04-04", 1, 2)
