from django.db import models
from user.models import MyUser





class UserVital(models.Model):
    user                = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    heart_rate          = models.IntegerField(default = 0) # in bpm
    blood_pressure_up   = models.IntegerField(default = 0)
    blood_pressure_down = models.IntegerField(default = 0)
    respiration_rate    = models.IntegerField(default = 0)
    temprature          = models.DecimalField(max_digits=3, decimal_places=1, default = 0)
    
    def __str__(self):
        return self.user.username
    
    
    
class Appointments(models.Model):
    doctor  = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name= 'doctor')
    patient = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name= 'patient')
    
    def __str__(self):
        return self.patient.username