class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}"
