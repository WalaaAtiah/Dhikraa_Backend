from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Quiz(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE, null=True, blank=True)
    type=models.CharField(max_length=255)
    question = models.TextField(default="", null=True, blank=True)
    choices = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering=['-pk']

    