# this is api resonse message for successful case
async def api_success_response(data=None, message="Success", status_code=200):
    return {
        "status": status_code,
        "message": message,
        "data": data,
        "error": None
    }

# this is api resonse message for failure case
async def api_failure_response(message="Error", status_code=500, error=None):
    return {
        "status": status_code,
        "message": message,
        "data": None,
        "error": error
    }