from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    entity_name: str
    task_type: str
    time: str
    phone_number: str
    contact_person: str
    note: Optional[str] = None 
    status: str
    
class TaskCreate(TaskBase):
    date: datetime
    
    class Config:
        json_encoders = {
            datetime: lambda v:v.isoformat()
        }
        
class TaskUpdate(TaskBase):
    date: Optional[datetime] = None
    _id:str
    
class TaskResponse(TaskBase):
    _id: str
    
    class Config:
        json_encoders = {
            datetime: lambda v:v.isoformat()
        }