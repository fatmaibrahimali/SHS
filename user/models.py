from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .validid import ID_Valid



def validate_id(value):
    if ID_Valid(value).is_valid() == False:
         raise ValidationError(
            _('%(value)s is not valid id'),
            params={'value': value},
        )
        

class MyUser(AbstractUser):
    email = models.EmailField(verbose_name="email address", unique=True, blank=False, null=False)
    #user_type --> patient/employeee  --replaced with is_staff
    
    phone_regex = RegexValidator(regex="[0][1][0125][0-9][ ]?\d{3}[ ]?\d{4}", message="Phone number must be entered in the format: '01xx xxx xxxx'. Up to 11 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=11, unique=True, blank=False, null=False) # validators should be a list
    
    national_id = models.CharField(max_length=14 , validators=[validate_id] , unique=True, blank=False, null=False)
    
    REQUIRED_FIELDS = ['email', 'phone', 'national_id']

    def __str__(self):
        return self.username

   
    
class user_profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username
    
    
    