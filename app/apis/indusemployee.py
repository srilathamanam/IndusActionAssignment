
# this controller is for managing indus employee details

from fastapi import APIRouter, Depends, HTTPException
from app.database.supabaseconnection import supabase
from app.pydentic_models.employee import CreateEmployee, UpdateEmployee
from app.core.token_authentication import verify_token
from app.utils.api_response import api_failure_response, api_success_response
from app.services.indusemployeeservice import (
    add_employee_details,
    get_employee_details,
    update_employee_details,
    delete_employee_details,
    get_all_employee_details
)


router= APIRouter()

#this endpoint is for Login to get the autorized token

@router.post("/login-gettoken")
def login(email: str, password: str):
    response = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

    if response.user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": response.session.access_token,
        "token_type": "bearer"
    }

#this endpoint is for saving employee details in database
@router.post("/create-employee", dependencies=[Depends(verify_token)])
def add_employee(employee : CreateEmployee):
    try:
        result = add_employee_details(employee.dict())
        return api_success_response(result.data, "Employee created successfully")
    except Exception as e:
        return api_failure_response("Failed to create employee", 500, str(e))


#this endpoint is for getting one employee details
@router.get("/get-employee/{employeeuuid}", dependencies=[Depends(verify_token)])
def get_employee(employeeuuid:str):
    try:
        result = get_employee_details(employeeuuid)
        return api_success_response(result.data, "Get the employee data successfully")
    except Exception as e:
        return api_failure_response("Failed to get employee data", 500, str(e))


#this endpoint is for updating employee details
@router.put("/update-employee", dependencies=[Depends(verify_token)])
def update_employee(updateemployee : UpdateEmployee):
   try:
        result = update_employee_details(updateemployee)
        return api_success_response(result.data, "Updated employee data successfully")
   except Exception as e:
        return api_failure_response("Failed to update employee data", 500, str(e))

# this endpoint is for deleting employee details
@router.delete("/delete-employee/{employeeuuid}", dependencies=[Depends(verify_token)])
def delete_employee(employeeuuid : str):
    try:
        result = delete_employee_details(employeeuuid)
        return api_success_response(result.data, "Deleted employee data successfully")
    except Exception as e:
        return api_failure_response("Failed to delete employee data", 500, str(e))
    
#this endpoint is for getting all employee details
@router.get("/get-all-employees", dependencies=[Depends(verify_token)])
def get_all_employee():
    try:
        result = get_all_employee_details()
        return api_success_response(result.data, "Get all employees data successfully")
    except Exception as e:
        return api_failure_response("Failed to all employees data", 500, str(e))


