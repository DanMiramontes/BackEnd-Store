import json
import os
import pymysql
from dotenv import load_dotenv

load_dotenv()
HOST=os.environ['RDS_HOST']
USER=os.environ['USER_NAME']
PASSWORD=os.environ['PASSWORD']
DB=os.environ['DB_NAME'] 


def lambda_handler(event=None, context=None):
    if event and type(event) == int:
        try: 
            conection = pymysql.connect(host=HOST,user=USER,password=PASSWORD,db=DB)
            with conection.cursor() as cursor:
                cursor.execute('call store.sp_show_category(%s)',(event))
                row = cursor.fetchall()[0]
                category = Categories(name=str(row[1]),description=str(row[2]),id=int(row[0]),created_at=str(row[3]))
                result  = category.to_json()
            conection.close()
            return json.dumps({"status":"OK", "data":result})
            # {
            #  "status": "OK",
            #  "data": 
            #     {"id": 1, "item 1": "Audifonos", "description": "lorem", "created_at": "2023-07-06 17:49:15"}
            # }
        except:
            return json.dumps({"status":"Failer", "message":"ERROR"})
    
    else:
        try:
            connection = pymysql.connect(host=HOST,user=USER,password=PASSWORD,db=DB)
            categories = []
            with connection.cursor() as cursor:
                cursor.execute('call store.sp_index_category()')
                resultset = cursor.fetchall()
                for row in resultset:
                    category = Categories(name=str(row[1]),description=str(row[2]),id=int(row[0]),created_at=str(row[3]))
                    categories.append(category.to_json())
            connection.close()
            return json.dumps({"status":"OK", "data":categories},200)
            # {"status": "OK", "data": 
            #  [
            #    {"id": 1, "name": "item 1", "description": "lorem ", "created_at": "2023-07-06 17:49:15"}, 
            #    {"id": 2, "name": "item2", "description": "lorem", "created_at": "2023-07-06 20:38:56"}
            #  ]
            # }
            
        except:
            return json.dumps({"status":"Failer", "message":"ERROR"})
    
class Categories():
    def __init__(self,name, description,id=None,created_at=None):
        self.id:int = id
        self.name:str = name,
        self.description:str = description
        self.created_at:str = created_at

    def to_json(self,):
        return {
            'id': self.id,
            'name': self.name[0],
            'description': self.description,
            'created_at': self.created_at
        }


print(lambda_handler())