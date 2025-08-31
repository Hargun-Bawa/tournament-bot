class Player:
    def  __init__(self, name , id):
        self.name = name
        self.id = id
        self.score = 0
        self.record = []
        self.bye = False
        def __eq__ (self, val= int):
            print(self.name, val)
            return self.name == val
