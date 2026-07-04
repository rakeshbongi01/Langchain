from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Unknown"
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    cgpa: Optional[float] = Field(0, ge=0.0, le=4.0, description="CGPA must be between 0.0 and 4.0", example=3.5)
    #This is also correct
    #cgpa: Optional[float] = Field( ge=0.0, le=4.0, default=0.0)


student = Student(name="Alice")
print(student)
print("\n")

new_student = {"name": "Bob"}
student_from_dict = Student(**new_student)
print(student_from_dict)
print("\n")

student_with_default = Student()
print(student_with_default)

print("\n")
naya_student_with_age = Student(name="Charlie", age=20)
print(naya_student_with_age)

print("\n")
# Pydantic will try to convert the string '25' to an integer if possible
student_with_string_age = Student(name="David", age='25')
print(student_with_string_age)
print("\n")

# This will raise a validation error because '2s5' cannot be converted to an integer
#student_with_string_age = Student(name="David", age='2s5')
#print(student_with_string_age)


print("\n")
# This will raise a validation error because 'not-an-email' is not a valid email address
#student_with_invalid_email = Student(name="Eve", email='not-an-email')
#print(student_with_invalid_email)

print("\n")
student_with_valid_email = Student(name="Frank",email="frank@frankly.com")
print(student_with_valid_email)

print("\n")
student_with_valid_email = Student(name="Frank",email="frank@frankly.com", cgpa=3.5)
print(student_with_valid_email)


print("\n")
student_with_valid_email = Student(name="Frank",email="frank@frankly.com")
print(student_with_valid_email)