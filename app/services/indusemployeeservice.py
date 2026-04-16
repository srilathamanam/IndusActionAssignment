from app.database.supabaseconnection import supabase
from datetime import datetime

TABLE="employee"  # this is table in supabse 

# business logic to add employee details
def add_employee_details(createemployee):
    try:
        createemployee["created_at"]=datetime.utcnow().isoformat()
        return supabase.table(TABLE).insert(createemployee).execute()
    except Exception as e:
        raise Exception(f"Error while adding employee: {str(e)}")
    
# business logic to get one employee details
def get_employee_details(uuid : str):
    try:
        return supabase.table(TABLE).select().eq("uuid",uuid).execute()
    except Exception as e:
        raise Exception(f"Error while getting employee details: {str(e)}")

# business logic to update employee details
def update_employee_details(updateemployee):
    try:
        return supabase.table(TABLE).update(updateemployee).eq("uuid",updateemployee.uuid).execute()
    except Exception as e:
        raise Exception(f"Error while updating employee: {str(e)}")

# business logic to delete employee details
def delete_employee_details(uuid : str):
    #soft delete employee
    try:
        return supabase.table(TABLE).update({"active": False}).eq('uuid',uuid).execute()
    except Exception as e:
        raise Exception(f"Error while deleting employee: {str(e)}")

# business logic to get all employee details
def get_all_employee_details():
    try:
        return supabase.table(TABLE).select().execute()
    except Exception as e:
        raise Exception(f"Error while getting all employee: {str(e)}")
