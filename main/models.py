from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    created_by = models.CharField(max_length=150, null=True, blank=True, help_text="Username of the creator")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
