from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = {
        ('male', 'Male'),
        ('female', 'Female'),
    }
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default="20")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=False, default="male")
    # 1, 2 로 변환?
