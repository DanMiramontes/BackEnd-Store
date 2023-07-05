from src.database.db import connetcion_DB
from src.models.Products import Products

class ProductsServices():
    @classmethod
    def index_product(cls):
            try:
                connection = connetcion_DB()
                products = []
                with connection.cursor() as cursor:
                    cursor.execute('call store.sp_index_product()')
                    resultset = cursor.fetchall()
                    for row in resultset:
                        product = Products(name=str(row[1]),description=str(row[2]),id=int(row[0]),category=str(row[3]),created_at=str(row[4]))
                        products.append(product.to_json())        
                connection.close()
                return products
            except:
                 return None
            
    @classmethod
    def show_product(cls,id): 
            try: 
                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_show_product(%s)',(id))
                    row = cursor.fetchall()[0]
                    product = Products(name=str(row[1]),description=str(row[2]),id=int(row[0]),category=str(row[3]),created_at=str(row[4]))
                    result  = product.to_json()
                conection.close()
                return result
            except:
                 return None
    
    @classmethod       
    def create_product(cls,product): 
            try: 
                name = product.name[0]
                description = product.description
                category =product.category_id

                print(name)
                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_create_product(%s, %s,%s)',(name, description,category))
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
    def update_product(cls,id,product): 
            try: 
                name = product.name[0]
                description = product.description
                category =product.category_id

                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_update_product(%s,%s, %s,%s)',(id,name, description,category))
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
    def delete_product(cls,id): 
            try: 
                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_delete_product(%s)',(id))
                    row = cursor.fetchall()
                    conection.commit()
                conection.close()
                if row is True:
                     return True
                else: 
                     return None
            except:
                 return None
    
