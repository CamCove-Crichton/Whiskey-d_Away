from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """
    A model to capture all information pertaining to
    the user as well as booking history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_mobile_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the uder profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
