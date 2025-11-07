from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_skills = models.JSONField(default=list, blank=True)
    email = models.EmailField(blank=True , null=True)
    phone_number = models.CharField(max_length=20,blank=True ,null=True)


    def __str__(self):
        return f"{self.user.username} - {self.file.name}"
    