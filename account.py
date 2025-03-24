import os
import mysql.connector
from connexion_module import ConnexionModule
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

    def create_account(self, name_account, user_id):
        query = "INSERT INTO account (name_account, balance, id_user) VALUES (%s, %s, %s)"
        values = (name_account, 0,  user_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Compte crée.")
    
    def get_all_accounts_info(self, id_user):

        conn = ConnexionModule().get_connection()
        cursor = conn.cursor()

        query = "SELECT id_account, name_account, balance, id_user FROM account WHERE id_user = %s"
        values = (id_user,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()

        account_list = []
        for account in result :
            account_list.append({
                "id_account" : account[0],
                "name_account" : account[1],
                "balance" : account[2],
                "id_user" : account[3]
            })

        cursor.close()
        conn.close()

        print(account_list)
        return account_list

    def delete_account(self, id_account) :
        query = "DELETE FROM account WHERE id_account = %s"
        self.cursor.execute(query, (id_account,))
        self.conn.commit()
        print("compte supprimé.")

# account = Account()
# account_name = "Benj"

# account.create_account(account_name, 1)