from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    google_email = models.EmailField(null=False)

    def __str__(self):
        return self.user.username
