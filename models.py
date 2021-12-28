from pydantic import BaseModel


class OutputNeural(BaseModel):
    plate: str
    img_str: str
