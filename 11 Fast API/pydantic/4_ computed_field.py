from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
        name: str
        age: int
        email : EmailStr
        weight: float
        height: float
        married: bool
        allergies: List[str]
        contact_details: Dict['str','str']
        
        @computed_field
        @property
        def bmi(self) -> float:
                bmi = round(self.weight/(self.height**2),2)
                return bmi
        
        

def insert_patient_data(patient: Patient):
    
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.height)
        print(patient.bmi)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_details)
        print("inserted into database successfully")      
                
    
patient_info: str = {'name': 'John Doe', 'age': '30', 'email': 'john.doe@rbc.com', 'weight': 70.5, 'height': 1.72,
                     'married': True, 'allergies': ['pollen', 'nuts'],
                     'contact_details': {'email': 'john.doe@example.com'}, 'linkedin': 'https://www.linkedin.com/in/johndoe'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)