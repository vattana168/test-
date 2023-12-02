class Patient:
    def __init__(self, name, age, ailment):
        self.name = name
        self.age = age
        self.ailment = ailment
        self.status = "Checked Out"

    def check_in(self):
        self.status = "Checked In"

    def check_out(self):
        self.status = "Checked Out"

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Ailment: {self.ailment}, Status: {self.status}"
