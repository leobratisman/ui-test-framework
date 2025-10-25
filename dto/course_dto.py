from pydantic import BaseModel


class CreateCourseDataDTO(BaseModel):
    title: str
    description: str
    max_score: int
    min_score: int
    estimated_time: str

class CheckCourseWidgetDTO(BaseModel):
    index: int
    title: str
    max_score: int
    min_score: int
    estimated_time: str