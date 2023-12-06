from django.db import models

class user_registration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('NA', 'Prefer not to say'),
    ]
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=15,
        choices=GENDER_CHOICES,
        default='M',  # Set a default value if needed
    )
    email = models.EmailField()

    def __str__(self):
        return self.first_name