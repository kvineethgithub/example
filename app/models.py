from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name.username
