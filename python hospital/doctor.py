from staff import Staff

class Doctor(Staff):
    def __init__(self, name, specialty):
        super().__init__(name, "Doctor")
        self.specialty = specialty

    def __str__(self):
        return f"{super().__str__()}, Specialty: {self.specialty}"
