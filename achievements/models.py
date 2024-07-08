from django.db import models
from django.contrib.auth.models import User

class Achievement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    points = models.IntegerField()

class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)