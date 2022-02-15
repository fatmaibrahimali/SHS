from django.db import models
from user.models import MyUser


JOBLIST = [
    ('HR', 'HR'),
    ('Dr', 'Dr'),
    ('Nurse', 'Nurse'),
    ('Ph', 'Ph'),
]

DEGREELIST = [
    ('PH', 'PH'),
    ('colleague', 'colleague'),
    ('Master', 'Master'),
    ('Graduated', 'Graduated'),
]


class JobProfile(models.Model):
    user       = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    job        = models.CharField(choices= JOBLIST, max_length=20, default="None")
    expeience  = models.IntegerField(default=0)
    start_time = models.TimeField(default = '00:00:00')
    end_time   = models.TimeField(default = '00:00:00')
    degree     = models.CharField(choices= DEGREELIST, max_length=20, default="None")
    
    def __str__(self):
        return self.user.username
    
    
    