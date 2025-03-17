import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database="bank"
)