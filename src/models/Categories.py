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