class ToDoService:
    def __init__(self):
        self.model = self.ToDoModel()
        
    def create(self, params):
        self.model.create(params["text"], params["Description"])