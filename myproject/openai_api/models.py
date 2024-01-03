from django.db import models

class UserSession(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    model = models.CharField(max_length=50, default="text-davinci-003")
