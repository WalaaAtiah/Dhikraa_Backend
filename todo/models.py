from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class TODO(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    task=models.CharField(max_length=255)
    description= models.TextField(blank=True)
    date = models.DateField(null=True)
    time=models.TimeField(null=True)


    def __str__(self):
        return self.task

    class Meta:
        verbose_name_plural = "Tasks"
        ordering=['-pk']
