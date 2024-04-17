from django.apps import AppConfig
import os
from django.conf import settings



class ApplicantsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applicants"

    def ready(self):
        # Ensure upload directory exists
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
