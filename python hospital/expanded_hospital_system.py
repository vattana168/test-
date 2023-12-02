from patient_expanded import Patient
from staff import Staff
from doctor import Doctor
from hospital_expanded import Hospital

def main():
    hospital = Hospital()

    while True:
        print("\n--- Hospital System ---")
        print("1. Add Patient")
        print("2. Remove Patient")
        print("3. Add Staff")
        print("4. Remove Staff")
        print("5. Check-in Patient")
        print("6. Check-out Patient")
        print("7. Show Patients")
        print("8. Show Staff")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient's name: ")
            age = input("Enter patient's age: ")
            ailment = input("Enter patient's ailment: ")
            hospital.add_patient(Patient(name, age, ailment))
            print("")
        elif choice == '2':
            name = input("Enter the name of the patient to remove: ")
            hospital.remove_patient(name)
        elif choice == '3':
            name = input("Enter staff name: ")
            position = input("Enter staff position: ")
            hospital.add_staff(Staff(name, position))
        elif choice == '4':
            name = input("Enter the name of the staff to remove: ")
            hospital.remove_staff(name)
        elif choice == '5':
            name = input("Enter the name of the patient to check in: ")
            if hospital.check_in_patient(name):
                print("Patient checked in successfully.")
            else:
                print("Failed to check in patient.")
        elif choice == '6':
            name = input("Enter the name of the patient to check out: ")
            if hospital.check_out_patient(name):
                print("Patient checked out successfully.")
            else:
                print("Failed to check out patient.")
        elif choice == '7':
            print("\n--- Patients ---")
            hospital.show_patients()
        elif choice == '8':
            print("\n--- Staff ---")
            hospital.show_staff()
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
