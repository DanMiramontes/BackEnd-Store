from src.database.db import connetcion_DB
from src.models.Categories import Categories

class CategoriesService():
    @classmethod
    def index_categories(cls):
        try:
            connection = connetcion_DB()
            categories = []
            with connection.cursor() as cursor:
                cursor.execute('call store.sp_index_category()')
                resultset = cursor.fetchall()
                for row in resultset:
                    category = Categories(name=str(row[1]),description=str(row[2]),id=int(row[0]),created_at=str(row[3]))
                    categories.append(category.to_json())
            connection.close()
            return categories
        except:
            return None
        
    @classmethod
    def show_category(cls,id): 
        try: 
            conection = connetcion_DB()
            with conection.cursor() as cursor:
                cursor.execute('call store.sp_show_category(%s)',(id))
                row = cursor.fetchall()[0]
                category = Categories(name=str(row[1]),description=str(row[2]),id=int(row[0]),created_at=str(row[3]))
                result  = category.to_json()
            conection.close()
            return result
        except:
            return None
    @classmethod       
    def create_category(cls,category): 
        try: 
            name = category.name[0]
            description = category.description
            conection = connetcion_DB()
            with conection.cursor() as cursor:
                cursor.execute('call store.sp_create_category(%s, %s)',(name, description))
                row = cursor.fetchall()     
                conection.commit()
            conection.close()
            if row is True:
                return True
            else: 
                return None
        except:
            return None
    

    @classmethod       
    def update_category(cls,id,category): 
        try: 
            name = category.name[0]
            description = category.description
            conection = connetcion_DB()
            with conection.cursor() as cursor:
                cursor.execute('call store.sp_update_category(%s,%s, %s)',(id,name, description))
                row = cursor.fetchall()
                conection.commit()
            conection.close()
            if row is True:
                return True
            else: 
                return None
        except:
            return None

    @classmethod       
    def delete_category(cls,id): 
        try: 
            conection = connetcion_DB()
            with conection.cursor() as cursor:
                cursor.execute('call store.sp_delete_category(%s)',(id))
                row = cursor.fetchall()
                conection.commit()
            conection.close()
            if row is True:
                return True
            else: 
                return None
        except:
            return None
