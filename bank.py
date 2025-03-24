import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()


db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_database = os.getenv("DB_DATABASE")


mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS bank")
cursor.execute("USE bank") 

cursor.close()
mydb.close()

mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database="bank"
)

cursor = mydb.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    fname VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS account (
    id_account INT AUTO_INCREMENT PRIMARY KEY,
    name_account VARCHAR(50),
    balance INT NOT NULL,
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES user (id_user) ON DELETE CASCADE
);
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS transaction (
    id_transaction INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(200) NOT NULL,
    amount INT NOT NULL,
    date DATE NOT NULL,
    type ENUM('deposit', 'withdrawal', 'transfer') NOT NULL,
    account_id INT NOT NULL,
    FOREIGN KEY (account_id) REFERENCES account(id_account) ON DELETE CASCADE
);
""")


mydb.commit()
cursor.close()
mydb.close()

print("Base de données et tables créées avec succès.")
