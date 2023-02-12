from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=255)
    ID_of = models.IntegerField()
    Contact = models.IntegerField()
    Address =models.CharField(max_length=255)

    def __str__(self):
        return f'{self.Name}'   