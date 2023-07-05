class Order_detail():
    def __init__(self,purchase_order_id,product_id,quantity,total,id=None):
        self.purchase_order_id:int = purchase_order_id,
        self.product_id:int = product_id,
        self.quantity:int = quantity,
        self.total:int = total,
        self.id:int = id
