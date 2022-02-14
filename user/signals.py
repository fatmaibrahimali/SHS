from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyUser, UserProfile, UserVital
from .validid import ID_Valid




@receiver(post_save, sender=MyUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('*********************************')
        UserProfile.objects.create(
            user=instance,
            birth_date = ID_Valid(instance.national_id).get_birth(), # year-month-day
            sex = ID_Valid(instance.national_id).get_sex() # Male/Female
            )
        print('===============================')
        UserVital.objects.create(user=instance)
            

