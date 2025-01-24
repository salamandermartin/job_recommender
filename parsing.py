import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    skills = ["Python", "Machine Learning", "JavaScript", "SQL", "AWS"]
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    return found_skills

def parse_resume(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    doc = nlp(text)
    extracted_skills = extract_skills(text)
    experience = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    return {"skills": extracted_skills, "experience": experience}

print(parse_resume("resume.txt"))