from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
        name: str
        age: int
        email : EmailStr
        weight: float
        married: bool
        allergies: List[str]
        contact_details: Dict['str','str']
        linkedin: AnyUrl
        
        @field_validator('email')
        @classmethod
        def email_validation(cls, value):

                valid_domain = ['hdfc.com','rbc.com']
                
                domain_name = value.split('@')[-1]
                
                if domain_name not in valid_domain:
                    raise ValueError('Not a Valid domain')
                
                return value
            
        @field_validator('name')
        @classmethod
        def transform_name(cls, value):
                 return value.upper()
             
             
        @field_validator('age', mode='after')
        @classmethod
        def validate_age(cls, value):
                if 0 < value < 100:
                    return value
                else:
                    raise ValueError("age should be between 0 and 100")
                

def insert_patient_data(patient: Patient):
    
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_details)
        print("inserted into database successfully")      
                
    
patient_info: str = {'name': 'John Doe', 'age': '30', 'email': 'john.doe@rbc.com', 'weight': 70.5, 
                     'married': True, 'allergies': ['pollen', 'nuts'],
                     'contact_details': {'email': 'john.doe@example.com'}, 'linkedin': 'https://www.linkedin.com/in/johndoe'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)