from staff import staff
from read_csv import *
from hod import *
from hod_CRED import *
from helper import *

# Assume validation functions are already defined:
# validate_empid(empid), validate_salary(salary), validate_name(name), validate_choice(options)

def main_menu():
    print("\n Welcome to Staff Management System")
    print("1. HOD Login")
    print("2. Staff Login")
    print("3. Exit")
    
    while True:
        try:
            choice = validate_choice(['1', '2', '3'], "Enter your choice: ")
            return choice
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid choice.")

def hod_menu():
    hod_ = hod()
    cred_ = cred()
    while True:
        print("\n  HOD Menu")
        print("1. Staff Management")
        print("2. Correction Request")
        print("3. Log out")
        
        try:
            choice = validate_choice(['1', '2', '3'], "Enter Your Choice: ")
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid choice.")
            continue

        if choice == "1":
            print("\n Staff Management")
            print("1. View Staff details")
            print("2. Add New Staff")
            print("3. Delete A Staff")
            print("4. Edit Staff Details")
            print("5. Log out")

            try:
                sub_choice = validate_choice(['1', '2', '3', '4', '5'], "Enter Your Choice: ")
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid choice.")
                continue

            if sub_choice == "1":
                print("For Entire Details Just Press Enter Or For Specific Details Enter Staff ID")
                empid = input("Enter the Staff Id (or press Enter for all): ").strip()
                if empid:
                    try:
                        empid = validate_empid(int(empid))
                        cred_.read_staff_details(empid)
                    except ValueError as e:
                        print(f"Error: {e}. Please enter a valid Staff ID.")
                        continue
                else:
                    cred_.read_staff_details()

            elif sub_choice == "2":
                name = input("Enter the name of the employee: ").strip()
                try:
                    empid = int(input("Enter the employee ID: ").strip())
                    empid = validate_empid(empid)
                except ValueError as e:
                    print(f"Error: {e}. Please enter a valid Employee ID.")
                    continue
                position = input("Enter The Position: ").strip()
                try:
                    salary = input("Enter Salary: ")
                    salary = validate_salary(int(salary))
                except ValueError as e:
                    print(f"Error: {e}. Please enter a valid Salary.")
                    continue
                
                name = validate_name(name)
                staff_details = staff()
                staff_details.add_employ(empid, name, position, salary)
                add_to_csv(staff_details)

            elif sub_choice == "3":
                try:
                    empid = int(input("Enter staff ID: ").strip())
                    empid = validate_empid(empid)
                    cred_.delete_a_staff(empid)
                except ValueError as e:
                    print(f"Error: {e}. Please enter a valid Staff ID.")
                    continue

            elif sub_choice == "4":
                try:
                    empid = int(input("Enter staff ID: ").strip())
                    empid = validate_empid(empid)
                except ValueError as e:
                    print(f"Error: {e}. Please enter a valid Staff ID.")
                    continue

                print("Options:")
                print("1. Change Staff ID")
                print("2. Change Name")
                print("3. Change Designation")
                print("4. Change Salary")
                try:
                    field_choice = validate_choice(['1', '2', '3', '4'], "Enter your choice: ")
                except ValueError as e:
                    print(f"Error: {e}. Please enter a valid choice.")
                    continue

                field = ''
                if field_choice == "1":
                    field = 'Staff ID'
                elif field_choice == "2":
                    field = 'Name'
                elif field_choice == "3":
                    field = 'Designation'
                elif field_choice == "4":
                    field = 'Salary'
                try:    
                    new_value = input(f"Enter The New Value For {field}: ")
                    if field=='Salary':
                        new_value=validate_salary(new_value)
                    elif field=='Name':
                        new_value=validate_name(new_value)
                    elif field=='Staff ID':
                        new_value=validate_empid(new_value)           
                    cred_.edit_staff_details(empid, field, new_value)
                    break
                except ValueError as e:
                    print(e)

            elif sub_choice == "5":
                break

            else:
                print("Invalid choice. Please try again.")
                continue

        elif choice == "2":
            hod_.reading_request()
            print("Option")
            print("1: For Proceed")
            print("2: For Exit")
            try:
                request = validate_choice(['1', '2'], "Enter Your Choice: ")
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid choice.")
                continue

            if request == "1":
                hod_.identify_issue()
            else:
                print("Request Denied")
                continue

        elif choice == "3":
            break

def staff_menu(staffid=None):
    if staffid is None:
        while True:
            try:
                staffid = int(input("Enter your Staff ID: ").strip())
                staffid = validate_empid(staffid)
                break
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid Staff ID.")
                continue

    while True:
        print("\n Staff Menu")
        print("Options:")
        print("1. Your Profile")
        print("2. Raise A Request")
        print("3. Log out")
        try:
            staff_req = validate_choice(['1', '2', '3'], "Enter your choice: ")
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid choice.")
            continue

        if staff_req == "1":
            print("Welcome To Your Profile")
            get_staff_details(staffid)
            continue

        elif staff_req == "2":
            print("Options:")
            print("1. Change Name")
            print("2. Change Designation")
            print("3. Change Salary")
            try:
                field_choice = validate_choice(['1', '2', '3'], "Enter your choice: ")
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid choice.")
                continue
            
            field = ''
            if field_choice == "1":
                field = 'Name'
            elif field_choice == "2":
                field = 'Designation'
            elif field_choice == "3":
                field = 'Salary'

            reason = input("Enter The Reason To Make Change: ")
            new_value = input("Enter The New Value To Change: ")
            if field=='Name':
                new_value=validate_name(new_value)
            elif field=='Salary':
                new_value=validate_salary(new_value)   
            staff_details = staff()
            staff_details.raise_request(staffid, field, reason, new_value)
            continue

        elif staff_req == "3":
            break

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            hod_menu()
        elif choice == "2":
            staff_menu()
        elif choice == "3":
            print("Exiting From System \n Have a nice day")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
