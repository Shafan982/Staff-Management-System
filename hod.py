import csv
import os

correction_file_path = r"c:/Users/DELL/Desktop/python/staff_managment _system/correction.csv"
staff_details_file_path = r"c:/Users/DELL/Desktop/python/staff_managment _system/staff_details.csv"

class hod:
    def reading_request(self): 
        try:
            with open(correction_file_path, mode='r') as file:
                reader = csv.reader(file)
                print("Requests from the file:")
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print(f"Error: The file '{correction_file_path}' does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def identify_issue(self):
        try:
            # Open the correction file
            with open(correction_file_path, mode='r') as correction_file:
                reader = csv.DictReader(correction_file)
                correction_rows = list(reader)
                correction_fieldnames = reader.fieldnames
        except Exception as e:
            print(f"Error reading correction file: {e}")
            return

        try:
            # Open the staff details file
            with open(staff_details_file_path, mode='r') as staff_file:
                staff_reader = csv.DictReader(staff_file)
                staff_rows = list(staff_reader)
                staff_fieldnames = staff_reader.fieldnames
        except Exception as e:
            print(f"Error reading staff details file: {e}")
            return

        updated = False
        unprocessed_corrections = []

        for correction_row in correction_rows:
            staff_id = correction_row['Staff ID']
            request_type = correction_row['Request Type'].title()
            corrected_value = correction_row['Corrected Value']

            update = False  # Reset update for each correction row

            for row in staff_rows:
                if row['Staff ID'] == staff_id:
                    if request_type == "Salary":
                        row["Salary"] = corrected_value
                        update = True
                    elif request_type == "Staff ID":
                        row["Staff ID"] = corrected_value
                        update = True
                    elif request_type == "Name": 
                        row["Name"] = corrected_value
                        update = True
                    elif request_type == "Designation":
                        row["Designation"] = corrected_value
                        update = True
                    break

            if not update:
                unprocessed_corrections.append(correction_row)
            else:
                updated = True

        # Write back to staff details file if updates were made
        if updated:
            try:
                with open(staff_details_file_path, mode='w', newline='') as staff_file:
                    writer = csv.DictWriter(staff_file, fieldnames=staff_fieldnames)
                    writer.writeheader()
                    writer.writerows(staff_rows)
                print("Main file has been updated.")
            except Exception as e:
                print(f"Error writing to the staff details file: {e}")

        # Write back unprocessed corrections to correction file
        try:
            with open(correction_file_path, mode='w', newline='') as correction_file:
                writer = csv.DictWriter(correction_file, fieldnames=correction_fieldnames)
                writer.writeheader()
                writer.writerows(unprocessed_corrections)
                print("Processed corrections have been removed from the correction file.")
        except Exception as e:
            print(f"Error occurred while updating the correction file: {e}")

        if not updated:
            print("No updates were made.")
