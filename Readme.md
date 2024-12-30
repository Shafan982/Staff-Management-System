# Staff Management System

## Overview
The Staff Management System is a Python-based application designed to efficiently manage staff-related operations, including staff registration, profile management, and correction requests. The system provides a user-friendly interface for both HODs and staff members, enabling streamlined administrative tasks and data handling.

## Features

### HOD Functions
- **Staff Management**:
  - View staff details (all or specific by Staff ID).
  - Add new staff members to the system.
  - Edit staff details (Name, Designation, Salary, etc.).
  - Delete staff records.
- **Correction Request Handling**:
  - View and process requests raised by staff members.
  - Update staff details based on approved correction requests.

### Staff Functions
- **Profile Management**:
  - View individual staff profile details.
- **Raise Requests**:
  - Request updates to Name, Designation, or Salary.
  - Provide a reason for the requested change.

--- 

## System Requirements
- Python 3.7 or above
- Libraries:
  - `csv`
  - `datetime`
  - `os`

---

## File Structure
- `main.py`: Entry point for the application. Handles user interactions and menu navigation.
- `staff.py`: Defines the `Staff` class and its related functions (e.g., adding staff, raising requests).
- `hod.py`: Defines the `HOD` class and its functionalities (e.g., managing correction requests).
- `hod_CRED.py`: Implements functions to read, edit, and delete staff details.
- `read_csv.py`: Contains utility functions for reading and writing CSV files.
- `helper.py`: Contains validation functions for data inputs.
- `staff_details.csv`: Stores staff information (e.g., ID, Name, Designation, Salary).
- `correction.csv`: Tracks correction requests made by staff.

---

## Setup Instructions

1. **Clone or Download**:
   Clone or download the repository to your local machine.

2. **Install Dependencies**:
   Ensure Python is installed on your system.

3. **Directory Structure**:
   Place the following files in the specified paths:
   - `staff_details.csv`: `c:/Users/DELL/Desktop/python/staff_management_system/staff_details.csv`
   - `correction.csv`: `c:/Users/DELL/Desktop/python/staff_management_system/correction.csv`

4. **Run the Application**:
   Execute the `main.py` file using the command:
   ```bash
   python main.py
   ```

---

## Usage Instructions

### Main Menu
1. **HOD Login**: Access HOD-specific operations.
2. **Staff Login**: Access staff-specific operations.
3. **Exit**: Exit the application.

### HOD Menu
- **Staff Management**:
  - View, Add, Edit, or Delete staff details.
- **Correction Request**:
  - View and process correction requests.
- **Log Out**: Return to the main menu.

### Staff Menu
- **Your Profile**: View your personal staff profile.
- **Raise a Request**: Submit requests for changes in Name, Designation, or Salary.
- **Log Out**: Return to the main menu.

---

## Data Validation
- **Staff ID**: Must be a 4-digit integer (e.g., 1234).
- **Name**: Must contain only alphabets.
- **Salary**: Must be a positive integer.

---

## Error Handling
- Handles `FileNotFoundError` for missing CSV files.
- Validates user inputs for correctness and appropriate formats.
- Prevents duplicate or invalid entries in staff details.

---
## Future Improvements
- Integrate a database system for improved scalability.
- Add a GUI for enhanced user experience.
- Implement authentication for HOD and staff logins.

---