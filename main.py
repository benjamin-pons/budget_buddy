from bank import *
from connexion_module import *
from account import *

email = "benjamin@exemple.fr"
mot_de_passe = "Azerty/pp1"

conn = ConnexionModule()

if conn.check_user(email, mot_de_passe):
    print("Connexion réussie !")
else:
    print("Échec de la connexion. Identifiants incorrects.")
 