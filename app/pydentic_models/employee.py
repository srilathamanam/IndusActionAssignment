from pydantic import BaseModel, Field
from typing import Optional

# this is request object to save emplaoyee details
class CreateEmployee(BaseModel):
    name : str = Field(..., min_length=8, max_length=20, description="Name allows 8 to 20 charaters")
    email : str = Field(..., description="Give valid email")
    salary : float =Field(..., gt=0, description="Salary must be greater than 0")

#this is request object to update employee details
class UpdateEmployee(BaseModel):
    employeeuuid: str = Field(..., min_length=5, description="Give valid employee uuis")
    name : Optional[str] = Field(None, min_length=8, max_length=20)
    email : Optional[str]
    salary : Optional[float]

