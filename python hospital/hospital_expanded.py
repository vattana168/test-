from patient_expanded import Patient
from staff import Staff
from doctor import Doctor

class Hospital:
    def __init__(self):
        self.patients = []
        self.staff = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, name):
        self.patients = [p for p in self.patients if p.name != name]

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def remove_staff(self, name):
        updated_staff = []
    for staff_member in self.staff:
        if staff_member.name != name:
            updated_staff.append(staff_member)
    self.staff = updated_staff

    def check_in_patient(self, name):
        patient = next((p for p in self.patients if p.name == name), None)
        if patient:
            patient.check_in()
            return True
        return False

    def check_out_patient(self, name):
        patient = next((p for p in self.patients if p.name == name), None)
        if patient:
            patient.check_out()
            return True
        return False              

    def show_patients(self):
        for patient in self.patients:
            print(patient)

    def show_staff(self):
        for staff_member in self.staff:
            print(staff_member)
