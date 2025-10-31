from pydantic import BaseModel, validator
import re


class DogResponse(BaseModel):
    breed: str
    image: str | None = None


class ExternalDog(BaseModel):
    breed: str
    image: str | None = None

    @validator("breed", pre=True, always=True)
    def clean_breed(cls, v, values):
        url_match = re.search(r"https?://\S+", v)
        if url_match:
            values["image"] = url_match.group(0)
            return re.sub(r"https?://\S+", "", v).strip()
        return v

    class Config:
        orm_mode = True


class TotalDogs(BaseModel):
    total: int