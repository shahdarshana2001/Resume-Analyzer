from celery import Celery
import time


celery_app = Celery(
    "resume_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)


@celery_app.task
def analyze_resume(name: str, resume_text: str):
    time.sleep(5)

    skills = ["Python", "FastAPI", "Celery", "Docker", "Machine Learning", "SQL"]

    found_skills = []
    for skill in skills:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    word_count = len(resume_text.split())

    return {
        "candidate_name": name,
        "word_count": word_count,
        "skills_found": found_skills,
        "summary": f"{name}'s resume contains {word_count} words and includes {len(found_skills)} relevant AI engineering skills."
    }