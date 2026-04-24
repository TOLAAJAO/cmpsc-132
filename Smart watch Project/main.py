# main.py

from person import Person
from medication import Medication
from contact import Contact

def display_welcome():
    print("\n====================================")
    print("   SMART ASSISTIVE WATCH SYSTEM")
    print("====================================")
    print("Welcome!")
    print("This system is designed to assist visually impaired users by providing safety alerts, reminders, and emergency support.")
    print("My goal is to promote independence and confidence in daily life.")
    print("Developed by Omotola Ajao")
    print("====================================\n")

def main():
    display_welcome()

    people = [
        Person(1, "Omotola", "Friend"), 
        Person(2, "Sarah", "Sister"),
        Person(3, "Mom", "Family")
    ]

    medications = [ 
        Medication("Insulin", "08:00"), 
        Medication("Vitamin C", "12:00"), 
        Medication("Painkiller", "20:00")
    ]

    contacts = [
        Contact("Mom","555-1234"), 
        Contact("Dad", "555-7672"), 
        Contact("Emergency Services", "911")
    ]

    while True:
        print("\n--- Smart Watch Menu ---")
        print("1. Detect Person")
        print("2. Medication Reminder")
        print("3. Emergency Call")
        print("4. Exit")
        choice = input("Enter option: ")

        if choice == "1":
            try: 
                detected_id = int(input("Enter detected person ID: "))
            except  ValueError:
                print("Invalid input. Please enter a number.")
                continue 

            found = False
            for person in people:
                if person.person_id == detected_id:
                    print(f"Person detected: {person.name} ({person.relationship})")
                    found = True
                    break
            if not found:
                print("Unknown person detected")
            input("\nPress Enter to return to menu...")
        
        elif choice == "2":
            current_time = input("Enter current time (HH:MM): ")
            found = False
            for med in medications:
                if med.time == current_time:
                    print(f"Reminder: Time to take your {med.name}")
                    found = True
            if not found:
                print("No medications scheduled at this time.")
            input("\nPress Enter to return to menu...")
        
        elif choice == "3":
            print("\nEmergency Contacts:")
            for i, contact in enumerate(contacts):
                print(f"{i + 1}. {contact.name} ({contact.phone})")
            try:
                 selection = int(input("Select contact to call: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if 1 <= selection <= len(contacts):
                chosen = contacts[selection - 1]
                print(f"Calling {chosen.name} at {chosen.phone}...")
            else:
                print("Invalid selection. Please choose a valid contact number")
            input("\nPress Enter to return to menu...")

        elif choice == "4":
            print("Exiting system ...")
            break
        else:
            print("Invalid choice. Try again.")
    

if __name__ == "__main__":
    main()