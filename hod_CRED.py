import csv
staff_details = r"c:/Users/DELL/Desktop/python/staff_managment _system/staff_details.csv"
class cred:
    def read_staff_details(self,staff_id=None):
        try:
            with open(staff_details,mode='r')as file:
                reader=csv.DictReader(file)
                if staff_id:
                    print(f"Search details of staffid:{staff_id}")
                    staff_id=str(staff_id).strip()
                    for row in reader:
                        if row['Staff ID'].strip() == staff_id:
                            print(row)
                            break
                    else:
                        print(f"No staff with this id:{staff_id}")
                            
                else:
                    print("All Staff Details")   
                    for row in reader:
                        print(row) 
                    
        except FileNotFoundError:
            print(print(f"Error: The file '{staff_details}' does not exist."))        
        except Exception as e:
            print(f"An error occuared {e}")    
            
    def delete_a_staff(self,staff_id):
        try:
            with open(staff_details,mode='r',)as file:
                reader=csv.DictReader(file)
                rows=list(reader)
                fieldnames=reader.fieldnames
                staff_id=str(staff_id).strip()
                
            new_rows= [row for row in rows if row['Staff ID']!= staff_id]   
            if len(new_rows)<len(rows):
                with open(staff_details,mode='w',newline='')as file:
                    writer=csv.DictWriter(file,fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(new_rows)
                print(f"Staff ID:{staff_id} is deleted from staff details")
            else:
                print(f"staff ID:{staff_id} not found")    
        except FileNotFoundError:
            print(f"Error: The file '{staff_details}' does not exist.")       
        except Exception as e:
             print(f"An unexpected error occurred: {e}")     
                
    def edit_staff_details(self,staff_id,field,new_value):
        try:
            if new_value is None:
                print("No update made: 'new_value' is None.")
                return
            with open(staff_details,mode='r')as file:
                reader=csv.DictReader(file)  
                rows=list(reader)
                fieldnames=reader.fieldnames
                
                updated=False
                staff_id=str(staff_id).strip()
                new_value=str(new_value).strip()
                for row in rows:
                    if row["Staff ID"]==staff_id:
                        if field in row:
                            row[field]=new_value
                            updated=True
                            print(f"Updated Staff ID {staff_id}: {field} -> {new_value}")
                        else:
                            print(f"Field '{field}' not found in the staff details.")  
                            return  
                if updated:
                    with open(staff_details,mode='w',newline='')as file:
                        writer=csv.DictWriter(file,fieldnames=fieldnames) 
                        writer.writeheader()    
                        writer.writerows(rows)
                    print(f"Staff ID {staff_id} has been updated in the staff details file.")
                else:
                    print(f"Staff ID {staff_id} not found.")          
        except FileNotFoundError:
            print(f"Error: The file '{staff_details}' does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")            