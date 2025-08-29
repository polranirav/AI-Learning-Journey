from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
from pathlib import Path
import json

app = FastAPI()
DATA_FILE = Path(__file__).with_name("patients.json")

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="id of the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="name of the patient", examples=["Nirav"])]
    city: Annotated[str, Field(..., description="city where patient lives")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="age of patient")]
    gender: Annotated[Literal["Male", "Female", "Others"], Field(..., description="gender of the patient")]
    height_m: Annotated[float, Field(..., gt=0, description="height (meters)")]
    weight_kg: Annotated[float, Field(..., gt=0, description="weight (kg)")]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight_kg / (self.height_m ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        bmi = self.bmi
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Healthy"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

class PatientUpdate(BaseModel):
    # optional fields must default to None
    name: Annotated[Optional[str], Field(None, description="name of the patient", examples=["Nirav"])]
    city: Annotated[Optional[str], Field(None, description="city where patient lives")]
    age: Annotated[Optional[int], Field(None, gt=0, lt=120, description="age of patient")]
    gender: Annotated[Optional[Literal["Male", "Female", "Others"]], Field(None, description="gender of the patient")]
    height_m: Annotated[Optional[float], Field(None, gt=0, description="height (meters)")]
    weight_kg: Annotated[Optional[float], Field(None, gt=0, description="weight (kg)")]

def load_data() -> dict:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}  # start empty if file doesn't exist

def save_data(data: dict) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.get("/")
def root():
    return {"message": "patient management system API"}

@app.get("/view")
def view():
    data = load_data()
    return {"data": data}

@app.post("/create")
def create_patient(p: Patient):
    data = load_data()
    if p.id in data:
        raise HTTPException(status_code=400, detail="patient already exists")

    # store by id; keep 'id' out of nested record since it's the key
    # (keeping bmi/verdict is OK; they get recomputed on update)
    data[p.id] = p.model_dump(exclude={"id"})
    save_data(data)
    return JSONResponse(status_code=201, content={"message": "patient created successfully"})

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="patient not found")
    return {"patient_id": patient_id, **data[patient_id]}

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='patient id not in data')

    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    # apply partial changes
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # rebuild Patient to recompute bmi/verdict (drop any stale computed fields first)
    existing_patient_info.pop('bmi', None)
    existing_patient_info.pop('verdict', None)
    existing_patient_info['id'] = patient_id

    patient_pydantic_obj = Patient(**existing_patient_info)

    # store back (exclude id; computed fields included, which is fine)
    data[patient_id] = patient_pydantic_obj.model_dump(exclude={'id'})
    save_data(data)

    return JSONResponse(status_code=202, content={'message': 'update patient'})



@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})
