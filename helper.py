# for ensure employ id is valid 4 digit integer 
def validate_empid(value):
    
    if isinstance(value, int) and 1000 <= value <= 9999:
        return value
    else:
        raise ValueError("Invalid Staff ID. Please ensure it is a 4-digit integer.")


# ensure name condain only alphabets
def validate_name(name):
    """Validate that the name contains only alphabets and is non-empty."""
    if name.isalpha():
        return name
    else:
        raise ValueError("Invalid name. Please ensure the name contains only alphabets.")

# salary only condain integer


def validate_salary(value):
    """Validates that the value is a valid salary (strictly numeric)."""
    if isinstance(value, int) and 1000 <= value <= 999999:
        return value
        if salary < 0:
            print("Salary cannot be negative.")
            return None
        return salary
    else:
        print("Invalid salary. Please enter only numeric values.")
        return None


# Validate choice1

def validate_choice(valid_choices, prompt):
    """Validate user input to ensure it matches one of the valid choices."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        else:
            raise ValueError(f"Invalid input. Please choose from {valid_choices}")
    
