from django.db import models
from django.contrib.auth.models import User

class UserProfile(User):
    student_id = models.CharField(max_length=255)
    gender = models.BooleanField()
