from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=100,title='name of the person', examples=['nirav','nikhil'])]  # Name must be a string with length constraints
    age: int
    email: EmailStr  # Validated email address
    weight: Annotated[float, Field(gt=0, le=300,strict=True)]  # Weight must be a float greater than 0 and less than or equal to 300
    married: bool  # Optional field with default value
    allergies: Annotated[Optional[List[str]], Field(max_length=5)] = None  # Optional list of allergies with a maximum of 5 items
    contact_details: Dict[str, str]  # Dictionary for contact details
    linkedin: Optional[AnyUrl] = None  # Validated URL
    

def insert_patient_data(patient: Patient):
    
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_details)
        print("inserted into database successfully")

def update_patient_data(patient: Patient):
    
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_details)
        print("updated into database successfully")

patient_info: str = {'name': 'John Doe', 'age': 30, 'email': 'john.doe@example.com', 'weight': 70.5, 
                     'married': True, 'allergies': ['pollen', 'nuts'],
                     'contact_details': {'email': 'john.doe@example.com'}, 'linkedin': 'https://www.linkedin.com/in/johndoe'}
patient1 = Patient(**patient_info)
    
insert_patient_data(patient1)
