from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ResumeSerializer
from .models import Resume
import pdfplumber
from docx import Document
import os
from .utils import extract_email,extract_phone,extract_skills

class ResumeUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            resume = serializer.save(user=request.user)
            file_path = resume.file.path
            text = ""

            try:
                
                if file_path.lower().endswith('.pdf'):
                    with pdfplumber.open(file_path) as pdf:
                        for page in pdf.pages:
                            text += page.extract_text() or ""

                
                elif file_path.lower().endswith('.docx'):
                    doc = Document(file_path)
                    for para in doc.paragraphs:
                        text += para.text + "\n"

                else:
                    text = "File format not supported for text extraction."

            except Exception as e:
                text = f"Could not extract text: {e}"

            skills = extract_skills(text)
            email = extract_email(text)
            phone = extract_phone(text)

            resume.extracted_skills = skills
            resume.email = email
            resume.phone_number = phone
            resume.save()



            return Response({
                "message": "Resume uploaded successfully",
                "resume_id": resume.id,
                "uploaded_at": resume.uploaded_at,
                "extracted_skills": skills,
                "email": email,
                "phone_number": phone,
                # "preview": text[:500] 
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
