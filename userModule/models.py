from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    question1 = models.CharField(blank=False, max_length=30)
    question2 = models.CharField(blank=False, max_length=30)
    answer1 = models.CharField(blank=False, max_length=30)
    answer2 = models.CharField(blank=False, max_length=30)

    def __str__(self):
        return self.username