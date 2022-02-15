from django.db.models.signals import post_save
from django.dispatch import receiver
from patient.models import UserVital
from staff.models import JobProfile
from .models import MyUser, UserProfile
from .validid import ID_Valid




@receiver(post_save, sender=MyUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            birth_date = ID_Valid(instance.national_id).get_birth(), # year-month-day
            sex = ID_Valid(instance.national_id).get_sex() # Male/Female
            )
        UserVital.objects.create(user=instance)
        if instance.is_staff:
            JobProfile.objects.create(user = instance)
            

