from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Application)
admin.site.register(models.ApplicationStatus)
admin.site.register(models.Job)
admin.site.register(models.UserProfile)