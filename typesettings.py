from enum import Enum
from pydantic import BaseModel, ValidationError


class Gender(str, Enum):
    male = "Male"
    female = "Female"
    unknown = "-"

class Config(BaseModel):
    gender: Gender