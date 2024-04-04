from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)  



class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posted_jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')  # Assuming resumes are uploaded as files
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.applicant.user.username} - {self.job.title}"


class ApplicationStatus(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=[
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.application} - {self.status}"
