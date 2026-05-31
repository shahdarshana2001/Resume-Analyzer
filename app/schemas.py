from pydantic import BaseModel


class ResumeRequest(BaseModel):
    name: str
    resume_text: str


class TaskResponse(BaseModel):
    task_id: str
    message: str