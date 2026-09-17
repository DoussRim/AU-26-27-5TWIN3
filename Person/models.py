from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
# Create your models here.
def VerifCin(value):
    if len(value)!=8:
        raise ValidationError('cin must have 8 characters')
def VerifEmail(value):
    if str(value).endswith('@esprit.tn'):
        raise ValidationError(f'you email {value} must end with @esprit.tn')
class Person(AbstractUser):
    cin=models.CharField("CIN",max_length=8,primary_key=True,validators=[VerifCin])
    email=models.EmailField(max_length=20,unique=True,validators=[VerifEmail])
    username=models.CharField(max_length=20,unique=True)
    
    USERNAME_FIELD="username"
    class Meta:
        #verbose_name="Personne"
        verbose_name_plural="List of Persons"