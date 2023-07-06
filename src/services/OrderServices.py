from src.database.db import connetcion_DB
from src.models.Orders import Orders

class OrderServices():
    @classmethod
    def index_order(cls):
            try:
                connection = connetcion_DB()
                orders = []
                with connection.cursor() as cursor:
                    cursor.execute('call store.sp_index_orders()')
                    resultset = cursor.fetchall()
                    for row in resultset:
                        order = Orders(provider_id=int(row[1]),date=str(row[2]),total=str(row[3]),id=int(row[0]),created_at=str(row[4]))
                        orders.append(order.to_json_index())
                connection.close()
                return orders
            except:
                 return None
    
    @classmethod
    def show_order(cls,id): 
            try: 
                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_show_order(%s)',(id))
                    row = cursor.fetchall()[0]
                    print(row)
                    order = Orders(
                         provider_id=int(row[1]),
                         name_prov=str(row[2]),
                         address_prov=str(row[3]),
                         date=str(row[4]),
                         total=int(row[5]),
                         created_at=str(row[6]),
                         id=int(row[0]))
                    result = order.to_json_show()
                conection.close()
                return result
            except:
                 return None

    @classmethod       
    def create_order(cls,order): 
            try: 
                provider = order.provider[0]
                total = order.total[0]
                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_create_orders(%s, %s)',(provider,total))
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
    def update_order(cls,id,order): 
            try: 
                provider = order.provider[0]
                total = order.total[0]

                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_update_order(%s,%s, %s)',(id,provider, total))
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
    def delete_order(cls,id): 
            try: 
                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_delete_order(%s)',(id))
                    row = cursor.fetchall()
                conection.commit()
                conection.close()
                if row is True:
                     return True
                else: 
                     return None
            except:
                 return None