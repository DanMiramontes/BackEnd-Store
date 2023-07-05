class Products():

    def __init__(self,name,description,category_id=None,id=None,created_at=None,category=None):
        self.id:int = id,
        self.name:str = name,
        self.description:str = description,
        self.category_id :int = category_id
        self.id: int = id
        self.created_at:str = created_at
        self.category:str = category



    def to_json(self,):
        return {
            'id': self.id,
            'name': self.name[0],
            'description': self.description[0],
            'category': self.category,
            'created_at': self.created_at
        }
