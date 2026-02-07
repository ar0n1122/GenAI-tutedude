# Task 3

class InvalidAgeError(ValueError):
    pass

def validate_age(age):
    if age<1 or age>120:
        raise InvalidAgeError("Age must be between 1 and 120.")
    return True

ages = [25, -5, 150, 30]
for age in ages:
    try:
        validate_age(age)
        print(f"Age {age} is valid.")
    except InvalidAgeError as e:
        print(f"Invalid age {age}: {e}")