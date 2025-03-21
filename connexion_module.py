import os
import mysql.connector
import bcrypt
import re
from dotenv import load_dotenv

load_dotenv()

class ConnexionModule:
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
    
    def hash_password(self, password):
        salt = bcrypt.gensalt()  # Génère un sel unique
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password, salt 

    def check_user(self, email, password):
        try:
            query = "SELECT password, salt FROM user WHERE email = %s"
            self.cursor.execute(query, (email,))
            result = self.cursor.fetchone()

            if result:
                hashed_password = result [0]
                if isinstance(hashed_password, str):
                    hashed_password = hashed_password.encode('utf-8')
                return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
            else:
                return False
            
        except mysql.connector.Error as err:
            print(f"Erreur : {err}")
            return False
    
    def get_user_id(self, email) :
        query = "SELECT id_user FROM user WHERE email = %s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()
        return result[0]

    def get_user_info(self, user_id) :
        query = "SELECT id_user, fname, name, email FROM user WHERE id_user = %s"
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        result_dict = {
            "user_id" : result[0],
            "fname" : result[1],
            "name" : result[2],
            "email" : result[3]
        }
        return result_dict
        
    def create_user(self, email, password, name, fname):
        if len(password) < 10:
            print("Erreur : mot de passe inférieur à 10 caractères.")
            return
        elif ' ' in password:
            print("Erreur : le mot de passe contient un espace.")
            return
        elif any(char.isupper() for char in password) and any(char.islower() for char in password) and bool(re.search(r'[^a-zA-Z0-9]', password)) and bool(re.search(r'\d', password)):
            print("Mot de passe valide.")
        else:
            print("Erreur : mot de passe invalide.")
            return

        hashed_password, salt = self.hash_password(password)  

        query = "INSERT INTO user(name, fname, email, password, salt) VALUES(%s, %s, %s, %s, %s)"
        values = (name, fname, email, hashed_password, salt)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Utilisateur créé.")

    def delete_user(self, id_user):
        query = "DELETE FROM user WHERE id_user = %s"
        self.cursor.execute(query, (id_user,))
        self.conn.commit()
        print("Compte utilisateur supprimé.")