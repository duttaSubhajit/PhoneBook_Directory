# phonebook/models.py

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
