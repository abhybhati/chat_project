import re

SKILLS_DB = ["Python","Django","DRF","MySql","Pandas","NumPy","JavaScript","REST API"]

def extract_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    match = re.search(email_pattern, text)
    return match.group(0) if match else None

def extract_phone(text):
    phone_pattern = r'\+?\d[\d -]{8,12}\d'
    match = re.search(phone_pattern , text)
    return match.group(0) if match else None

def extract_skills(text):
    found_skills = [skill for skill in SKILLS_DB if skill.lower() in text.lower()]
    return found_skills