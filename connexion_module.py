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
            self.cursor = self.conn.cursor()  # Retourne les résultats sous forme de dictionnaire
        except mysql.connector.Error as err:
            print(f"Erreur de connexion à la base de données : {err}")
            self.conn = None
    
    def hash_password(self, password) :
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def check_user(self, email, password):
        try:
            query = "SELECT password FROM user WHERE email = %s"
            self.cursor.execute(query, (email,))
            result = self.cursor.fetchone()

            if result:
                hashed_password = result[0]

                if isinstance(hashed_password, bytes):
                    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
                else:
                    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
            else:
                return False
            
        except mysql.connector.Error as err:
            print(f"Erreur : {err}")
            self.conn = None
        
    def create_user(self, email ,password, name, fname):
        if len(password) < 10 :
            print("Erreur mot de passe inférieur à 10 caracères")
            return
        elif ' ' in password :
            print("Erreur mot de passe contient un espace")
            return
        elif any(char.isupper() for char in password) and any(char.islower() for char in password) and bool(re.search(r'[^a-zA-Z0-9]', password)) and bool(re.search(r'\d', password)):
            print("Mot de pass valide")
        else :
            print("Erreur mot de pass invalide")
            return

        hash = self.hash_password(password)
        query = "INSERT INTO user(name, fname, email, password) VALUES(%s,%s,%s,%s)"
        values = (name, fname, email, hash)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Utilisateur créé")

    def delete_user(self, id_user) :
        query = "DELETE FROM user WHERE id_user = %s"
        self.cursor.execute(query, (id_user,))
        self.conn.commit()
        print("compte utlisateur supprimé.")
        

    



email = "benjamin@exemple.fr"
mot_de_passe = "Azerty/pp1"
name = "nam"
fname = "fname"


conn = ConnexionModule()


conn.create_user(email, mot_de_passe, name, fname)


user_delete = 1
# conn.delete_user(user_delete)

# if conn.check_user(email, mot_de_passe):
#     print("Connexion réussie !")
# else:
#     print("Échec de la connexion. Identifiants incorrects.")

