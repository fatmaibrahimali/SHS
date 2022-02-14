from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .validid import ID_Valid


BLOOD = [
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
    ('O+','O+'),
    ('O-','O-'),
    ]

SOCIAL =[
    ('single','single'),
    ('married','married'),
    ('divorced','divorced')
    ]


SEX =[
    ('Male','Male'),
    ('Female','Female'),
    ('Unknown','Unknown')
    ]



def validate_id(value):
    if ID_Valid(value).is_valid() == False:
         raise ValidationError(
            _('%(value)s is not valid id'),
            params={'value': value},
        )
        

class MyUser(AbstractUser):
    email       = models.EmailField(verbose_name="email address", unique=True, blank=False, null=False)
    #user_type --> patient/employeee  --replaced with is_staff
    phone_regex = RegexValidator(regex="[0][1][0125][0-9][ ]?\d{3}[ ]?\d{4}", message="Phone number must be entered in the format: '01xx xxx xxxx'. Up to 11 digits allowed.")
    phone       = models.CharField(validators=[phone_regex], max_length=11, unique=True, blank=False, null=False) # validators should be a list
    national_id = models.CharField(max_length=14 , validators=[validate_id] , unique=True, blank=False, null=False)
    
    REQUIRED_FIELDS = ['email', 'phone', 'national_id']

    def __str__(self):
        return self.username

   
    
class UserProfile(models.Model):
    user            = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    birth_date      = models.DateField(auto_now=False, auto_now_add=False)
    sex             = models.CharField(choices= SEX , max_length= 7)
    
    first_name      = models.CharField(max_length=20, default = 'first_name')
    last_name       = models.CharField(max_length=20, default = 'last_name')
    weight          = models.DecimalField(max_digits=6, decimal_places=3, default = 0) # in KG   
    height          = models.DecimalField(max_digits=4, decimal_places=1, default = 0) # in CM
    marital_status  = models.CharField(choices=SOCIAL , max_length= 8, default = "Ba2s")
    blood_type      = models.CharField(choices=BLOOD, max_length= 3, default = "Non")
    
    
    def __str__(self):
        return self.user.username
    
    

class UserVital(models.Model):
    user                = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    heart_rate          = models.IntegerField(default = 0) # in bpm
    blood_pressure_up   = models.IntegerField(default = 0)
    blood_pressure_down = models.IntegerField(default = 0)
    respiration_rate    = models.IntegerField(default = 0)
    temprature          = models.DecimalField(max_digits=3, decimal_places=1, default = 0)
    
    def __str__(self):
        return self.user.username