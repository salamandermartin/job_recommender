from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from parsing import extract_skills

app = FastAPI()

class ResumeData(BaseModel):
    skills: list
    experience: list

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    skills = extract_skills(content.decode("utf-8"))
    return {"filename": file.filename, "skills": skills}

@app.get("/recommend_jobs/")
def recommend_jobs():
    # Simulated job recommendations
    return {"jobs": ["Python Developer", "ML Engineer"]}