from django.db import models


# Create your models here.
class Contact(models.Model):
    name    = models.CharField(max_length=50)
    company = models.CharField(max_length=100, blank=True)
    phone   = models.CharField(max_length=11)
    email   = models.EmailField()
    message = models.TextField()

    def __str__(self):
        if self.name is not None:
            return self.name
