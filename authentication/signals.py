from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from authentication.models import UserProfile


@receiver(post_save, sender=SocialAccount)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, _ = UserProfile.objects.get_or_create(user=instance.user)
        full_name = instance.extra_data.get('name')
        google_email = instance.extra_data.get('email')

        if full_name:
            profile.full_name = full_name
            
        if google_email:
            profile.google_email = google_email
            
        profile.save()
