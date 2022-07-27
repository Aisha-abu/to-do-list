from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
