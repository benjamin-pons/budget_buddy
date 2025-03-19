from bank import *
from connexion_module import *

email = "benjamin@exemple.fr"
mot_de_passe = "$2b$12$3h21KbJZ4ZZ7H2d7PLFlFuA7AeJZ8uVO9NH87lZDXFjhuC7sznJZK"

conn = ConnexionModule()

if conn.check_user(email, mot_de_passe):
    print("Connexion réussie !")
else:
    print("Échec de la connexion. Identifiants incorrects.")
 