import csv
from datetime import datetime
import os
class staff:
    def add_employ(self,staff_id,name,designation,salary):
        self.staff_id=staff_id
        self.name=name
        self.designation=designation
        self.salary=salary
    @staticmethod
    def raise_request(staff_id,request_type,reason,corrected_value,request_file=r"c:/Users/DELL/Desktop/python/staff_managment _system/correction.csv"):
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S") #string format time is used to get time that printing type like we need
        file_exists = os.path.exists(request_file)
        with open(request_file,mode='a+',newline='')as file:
            writer=csv.writer(file)
            if not file_exists or file.tell()==0: 
                writer.writerow(["Staff ID","Request Type", "Reason","Corrected Value" ,"Timestamp"])
            writer.writerow([staff_id, request_type, reason,corrected_value, time]) 
        print(f"Request from Staff ID {staff_id} has been successfully raised .")       









