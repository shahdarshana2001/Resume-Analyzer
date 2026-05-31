from fastapi import FastAPI
from celery.result import AsyncResult

from app.schemas import ResumeRequest
from app.tasks import analyze_resume, celery_app

app = FastAPI(title="AI Resume Analyzer")


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API is running"}


@app.post("/analyze-resume")
def submit_resume(data: ResumeRequest):
    task = analyze_resume.delay(data.name, data.resume_text)

    return {
        "task_id": task.id,
        "message": "Resume analysis started. Use task_id to check result.",
    }


@app.get("/result/{task_id}")
def get_result(task_id: str):
    result = AsyncResult(task_id, app=celery_app)

    if result.state == "PENDING":
        return {"status": "PENDING", "message": "Task is still processing."}

    if result.state == "SUCCESS":
        return {"status": "SUCCESS", "result": result.result}

    return {"status": result.state, "message": "Task failed or is in another state."}