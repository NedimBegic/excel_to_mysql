import pymysql
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def get_db_connection():
    """Function to connect to MySQL database using PyMySQL with .env credentials."""
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        print("Connected to MySQL database")
        return connection

    except pymysql.MySQLError as e:
        print("Error while connecting to MySQL:", e)
        return None
