from pydantic import BaseModel 

class User(BaseModel):
    name: str
    email: str
    phone: str
    city: str
   # admin:bool

