from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=3000)