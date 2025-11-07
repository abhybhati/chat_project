def calculate_match(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)
    matched = resume_set & job_set
    missing = job_set - resume_set
    
    score = (len(matched) / len(job_set)) *100 if job_set else 0

    return {
        "score": round(score, 2),
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    }
    
