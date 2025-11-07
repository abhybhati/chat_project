from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from resumes.models import Resume
from jobs.models import Job
from rest_framework.permissions import IsAuthenticated


class ResumeJobMatchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            resume = Resume.objects.get(id=id, user=request.user)
        except Resume.DoesNotExist:
            return Response(
                {"error": "Resume not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        resume_skills = [skill.lower() for skill in resume.extracted_skills]
        matched_jobs = []

        for job in Job.objects.all():
            job_skills = [skill.lower() for skill in job.required_skills]
            common_skills = set(resume_skills) & set(job_skills)

            if common_skills:
                match_score = int((len(common_skills) / len(job_skills)) * 100)
                matched_jobs.append({
                    "job_id": job.id,
                    "title": job.title,
                    "matched_skills": list(common_skills),
                    "match_score": match_score
                })

        matched_jobs.sort(key=lambda x: x['match_score'], reverse=True)

        return Response({
            "resume_id": resume.id,
            "resume_skills": resume.extracted_skills,
            "matches": matched_jobs,
            "best_match": matched_jobs[0] if matched_jobs else None,
            "message": (
                f"Found {len(matched_jobs)} matching jobs."
                if matched_jobs else "No matching jobs found."
            )
        }, status=status.HTTP_200_OK)
