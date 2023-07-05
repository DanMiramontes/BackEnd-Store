class Providers():
    def __init__(self,name, full_address,id=None, created_at=None):
        self.id:int = id,
        self.name:str = name,
        self.full_address:str = full_address
        self.created_at:str = created_at
    
    def to_json(self,):
        return {
            'id': self.id[0],
            'name': self.name[0],
            'full_addres': self.full_address,
            'created_at': self.created_at
        }