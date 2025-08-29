
# Problem because not validation
def insert_patient_data(name, age):
        print(name)
        print(age)
        print("inserted into database successfully")
        
insert_patient_data("John Doe", 'thirty')

# code is working but not safe, we can pass any type of data
def insert_patient_data(name: str, age: int):
        print(name)
        print(age)
        print("inserted into database successfully")

insert_patient_data("John Doe", 30)

# little bit perfect method to validate data
def insert_patient_data(name: str, age: int):
    
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age cannot be negative")      
        else:
            print(name)
            print(age)
            print("inserted into database successfully")
    else:
            raise ValueError("Name must be a string and age must be an integer ")
insert_patient_data("John Doe", 30)    
def update_patient_data(name: str, age: int):
    
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("updated into database successfully")
    else:
        raise ValueError("Name must be a string and age must be an integer ")
# you have to write same code again and again for each function
# lot of data validation code you have to write it for every function if multiple perameters you are frustrated to write manual code
# pydantic is a data validation and settings management library for Python, based on type annotations.




