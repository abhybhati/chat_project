from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Job
from .serializers import JobSerializer

class JobCreateView(generics.CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)

class JobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [permissions.IsAuthenticated]

