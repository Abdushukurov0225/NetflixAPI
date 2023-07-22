from django.db import models

class Actor(models.Model):
    MALE = 'male'
    FAMALE = 'famale'

    GENDER = [
        (MALE, 'male'),
        (FAMALE, 'famale'),
    ]

    name = models.CharField(max_length=200, blank=False, null=False)
    birthdate = models.DateField(blank=True)
    gender = models.CharField(choices=GENDER, max_length=10,)


    def __str__(self):
        return self.name


