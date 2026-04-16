from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.database.supabaseconnection import supabase

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:       
        supabase.auth.set_session(access_token=token, refresh_token=token)

        user = supabase.auth.get_user()

        if user.user is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return user.user

    except Exception as e:
        print("Auth error:", str(e))   # debug
        raise HTTPException(status_code=401, detail="Invalid or expired token")