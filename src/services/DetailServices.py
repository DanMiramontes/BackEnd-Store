from src.database.db import connetcion_DB
from src.models.Detail import Order_detail,show_detail;

class DetailServices():
    @classmethod
    def index_order(cls):
        try:
            connection = connetcion_DB()
            orders = []
            with connection.cursor() as cursor:
                cursor.execute('call store.sp_index_order_detail()')
                resultset = cursor.fetchall()
                for row in resultset:
                    order = Order_detail(id=int(row[0]),purchase_order_id=str(row[1]),name=str(row[2]),quantity=row[3],total=row[4],created_at=row[5])
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
                cursor.execute('call store.sp_show_order_detail(%s)',(id))
                row = cursor.fetchall()[0]
                print(row)
                order = show_detail(detail_id=int(row[0]),detail_quantity=row[5],detail_total=row[6],
                                    product_name=str(row[1]),product_desc=str(row[2]),product_cat=str(row[3]),product_cat_des=str(row[4]),
                                    purchase_order=int(row[7]),purchase_date=str(row[8]),purchase_total=row[9],
                                    provider_name=str(row[10]),full_address=str(row[11])
                                    )
                result = order.to_json_show()
            conection.close()
            return result
        except:
            return None
    

    @classmethod       
    def create_detail(cls,detail): 
        try: 
            order_id = detail.purchase_order_id[0]
            product_id = detail.product_id[0]
            quantity = detail.quantity[0]
            total = detail.total[0]

            conection = connetcion_DB()
            with conection.cursor() as cursor:
                cursor.execute('call store.sp_create_orders_detail(%s, %s,%s,%s)',(order_id,product_id,quantity,total))
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
    def update_detail(cls,id,detail): 
        try: 
            quantity = detail.quantity[0]
            total = detail.total[0]
            print(quantity,total)

            conection = connetcion_DB()
            with conection.cursor() as cursor:
                cursor.execute('call store.sp_update_order_detail(%s, %s, %s)',(id,quantity,total))
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
    def delete_detail(cls,id): 
        try: 
            conection = connetcion_DB()
            with conection.cursor() as cursor:
                cursor.execute('call store.sp_delete_order_detail(%s)',(id))
                row = cursor.fetchall()
                conection.commit()
            conection.close()
            if row is True:
                return True
            else: 
                return None
        except:
            return None
