class Orders():
    def __init__(self,provider_id,date,total,id=None):
        self.provider:int = provider_id,
        self.date:str = date,
        self.total:int = total,
        self.id:int = id
        pass