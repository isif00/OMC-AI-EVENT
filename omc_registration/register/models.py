from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Participants(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    Matricule = models.IntegerField()
    publish_date = models.DateTimeField()

    class Meta:
        ordering = ['-publish_date'] 
        
    def __str__(self) -> str:
        return self.name