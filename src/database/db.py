from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

HOST=os.environ['MYSQL_HOST']
USER=os.environ['MYSQL_USER']
PASSWORD=os.environ['MYSQL_PASSWORD']
DB=os.environ['MYSQL_DB'] 


def connetcion_DB():
    try:
        return pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            db=DB
        )
    except: return pymysql.err