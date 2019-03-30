from django.db import models

# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length= 20)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField(unique=True)

    def __str__(self):
        return self.Email

