import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class Account():
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

    def create_account(self,name_account):
        query = "INSERT INTO account (name_account, balance)VALUES (%s, %s)"
        values = (name_account, 0)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("compte crée.")

    def delete_account(self, id_account) :
        query = "DELETE FROM account WHERE id_account = %s"
        self.cursor.execute(query, (id_account,))
        self.conn.commit()
        print("compte supprimé.")

account = Account()
account_name = "JUL"
id_account = 3

# account.delete_account(id_account)
account.create_account(account_name)
