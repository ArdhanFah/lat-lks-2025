from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_BASE_URL = os.getenv("API_BASE_URL")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/employees")
def get_employees():
    response = requests.get(f"{API_BASE_URL}/employees")
    return response.json()

@app.post("/api/employees")
def create_employee(employee: dict):
    response = requests.post(f"{API_BASE_URL}/employees", json=employee)
    return response.json()

@app.get("/api/employees/{employee_id}")
def get_employee(employee_id: str):
    response = requests.get(f"{API_BASE_URL}/employees/{employee_id}")
    return response.json()

@app.put("/api/employees/{employee_id}")
def update_employee(employee_id: str, employee: dict):
    response = requests.put(f"{API_BASE_URL}/employees/{employee_id}", json=employee)
    return response.json()

@app.delete("/api/employees/{employee_id}")
def delete_employee(employee_id: str):
    response = requests.delete(f"{API_BASE_URL}/employees/{employee_id}")
    return response.json()
