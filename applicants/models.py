from django.contrib.auth.models import User
from django.db import models

import random
import string

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    user_id2 = models.CharField(max_length=12, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.user_id2:
            self.user_id2 = self.generate_user_id2()
        super(UserProfile, self).save(*args, **kwargs)

    def generate_user_id2(self):
        """Generate a random string of letters and digits """
        char_set = string.ascii_letters + string.digits
        return ''.join(random.choice(char_set) for _ in range(12))



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
    resume = models.FileField(default = None, upload_to='resumes/')  # Assuming resumes are uploaded as files
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
