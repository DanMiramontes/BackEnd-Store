class Orders():
    def __init__(self,provider_id,total,date=None,id=None,created_at=None,name_prov=None, address_prov=None):
        self.provider:int = provider_id,
        self.date:str = date,
        self.total:int = total,
        self.id:int = id,
        self.created_at:str = created_at,
        self.name_prov:str = name_prov,
        self.addres_prov:str = address_prov

    def to_json_index(self,):
        return {
            'id': self.id[0],
            'provider_id': self.provider[0],
            'date': self.date[0],
            'total': self.total[0],
            'created_at': self.created_at[0]
        }
    def to_json_show(self,):
        return {
            'id': self.id[0],
            'provider': {
               'id' : self.provider[0],
               'name': self.name_prov[0],
               'address': self.addres_prov[0:],
            },
            'date': self.date[0],
            'total': self.total[0],
            'created_at': self.created_at[0]
        }