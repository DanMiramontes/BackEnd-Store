class Order_detail():
    def __init__(self,quantity,total,
                 product_id=None,id=None,name=None,created_at=None,purchase_order_id=None):
        self.purchase_order_id:int = purchase_order_id,
        self.product_id:int = product_id,
        self.quantity:int = quantity,
        self.total:int = total,
        self.id:int = id,
        self.name:str = name
        self.created_at:str = created_at


    def to_json_index(self,):
        return {
            'id': self.id[0],
            'order_id': self.purchase_order_id[0],
            'name': self.name,
            'quantity': self.quantity[0],
            'total': self.total[0],
            'created_at': self.created_at
        }
    

class show_detail():
    def __init__ (self, detail_id,detail_quantity,detail_total,
                  product_name, product_desc,product_cat,product_cat_des,
                  purchase_order,purchase_date, purchase_total,
                  provider_name, full_address) ->None:
        self.id = detail_id,
        self.quantity = detail_quantity,
        self.total =detail_total,
        self.name = product_name,
        self.description_prod = product_desc,
        self.category_prod = product_cat,
        self.cat_prod_des = product_cat_des,
        self.purchase_order_id = purchase_order,
        self.date_purchase = purchase_date,
        self.total_purchase = purchase_total,
        self.name_Prov = provider_name,
        self.full_address = full_address,
         
    def to_json_show(self,):
        return {
            'id': self.id[0],
            'product': {
                "name":self.name[0],
                "description":self.description_prod[0],
                "categoria": {
                    "name": self.category_prod[0],
                    "description":self.cat_prod_des[0],
                },
            },
            "purchase": {
                'order_id': self.purchase_order_id[0],
                'date': self.date_purchase[0],
                'total': self.total_purchase[0],
            },
            "provider":{
                "name": self.name_Prov[0],
                "address":self.full_address[0],
            },
            'quantity': self.quantity[0],
            'total': self.total[0],     
        }