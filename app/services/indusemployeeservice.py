from app.database.supabaseconnection import supabase
from datetime import datetime
import uuid

TABLE = "IndusEmployee" # this is table in supabse 

# business logic to add employee details
def add_employee_details(createemployee):
    try:
        employee_id = str(uuid.uuid4()) 
        createemployee["uuid"] = employee_id
        createemployee["created_at"]=datetime.utcnow().isoformat()
        response = supabase.table(TABLE).insert(createemployee).execute()
        return response
    except Exception as e:
        raise Exception(f"Error while adding employee: {str(e)}")
    
# business logic to get one employee details
def get_employee_details(employee_uuid : str):
    try:
        uuid_obj = str(uuid.UUID(employee_uuid)) 
        response = supabase.table(TABLE).select("*").eq("uuid", uuid_obj).execute()
        if not response.data:
            return {"message": "Employee not found", "data": None}
        return response
    except Exception as e:
        raise Exception(f"Error while getting employee details: {str(e)}")

# business logic to update employee details
def update_employee_details(updateemployee):
    try:
        uuid_obj = str(uuid.UUID(updateemployee.employeeuuid))

        existing = supabase.table(TABLE).select("*").eq("uuid", uuid_obj).execute()
        if not existing.data:
            return {"message": "Employee not found", "data": None}
        # take fileds which are not null
        update_data = updateemployee.model_dump(exclude={"employeeuuid"})
        # remove None values automatically
        update_data = {k: v for k, v in update_data.items() if v is not None}
        response = (
            supabase.table(TABLE)
            .update(update_data)
            .eq("uuid", uuid_obj)
            .execute()
        )
        return response

    except ValueError:
        return {"message": "Invalid UUID format", "data": None}

    except Exception as e:
        raise Exception(f"Error while updating employee: {str(e)}")

# business logic to delete employee details
def delete_employee_details(employee_uuid : str):
    #soft delete employee
    try:
        uuid_obj = str(uuid.UUID(employee_uuid))
        existing = supabase.table(TABLE).select("*").eq("uuid", uuid_obj).execute()
        if not existing.data:
            return {"message": "Employee not found", "data": None}
        return supabase.table(TABLE).update({"active": False}).eq("uuid", uuid_obj).execute()
    except Exception as e:
        raise Exception(f"Error while deleting employee: {str(e)}")

# business logic to get all employee details
def get_all_employee_details():
    try:
        return supabase.table(TABLE).select().execute()
    except Exception as e:
        raise Exception(f"Error while getting all employee: {str(e)}")
