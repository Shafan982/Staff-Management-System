import csv

# Function to add details into csv file
def add_to_csv(staff_member,file_name=r"c:/Users/DELL/Desktop/python/staff_managment _system/staff_details.csv"):
    try:
        with open(file_name,mode='a+',newline='') as file:
            writer=csv.writer(file)
            file.seek(0)  # point into the first line
            if not file.read(1): # read the first line if it is not available 
                writer.writerow(["Staff ID","Name","Designation","Salary"])
            writer.writerow([staff_member.staff_id,staff_member.name,staff_member.designation,staff_member.salary])
        print(f"Details of {staff_member.name} have been saved in staff_details.csv")          

    except FileNotFoundError:
        print("File staff_details.csv is not found")

# function to get staff details by giving staff id
def get_staff_details(staff_id,filename=r"c:/Users/DELL/Desktop/python/staff_managment _system/staff_details.csv"):
    try:
        with open(filename,mode='r')as file:
            reader=csv.reader(file)
            next(reader) # skip the header row
            found= False
            for a in reader:
               if len(a)>0 and a[0] == str(staff_id):
                   print(f" ID:{a[0]}\n Name:{a[1]}\n Designation:{a[2]}\n Salary:{a[3]}")
                   found=True
                   break
            if not found:   
                print(f"Staff with ID:{staff_id} not found")

    except FileNotFoundError:
        print("File staff_details.csv is not found")     




