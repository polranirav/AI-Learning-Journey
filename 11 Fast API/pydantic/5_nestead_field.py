from pydantic import BaseModel, ValidationError

class Address(BaseModel):
    
    city:str
    state: str
    pincode: int


class patient(BaseModel):
    
    name: str
    gender: str
    age: int
    address: object
    

address_dict = {'city': 'ahmedabad', 'state': 'Gujarat', 'pincode': '382350'}
address1 = Address(**address_dict)

patient_info = {'name': 'nirav', 'gender': 'male', 'age': '26', 'address': address1}
patient1 = patient(**patient_info)

print(patient1)


