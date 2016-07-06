from django.conf import settings
from django.db import models


class UserProfile(models.Model):

    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)

    given_name = models.CharField(max_length=255, blank=True, null=True)
    family_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True)
    birthdate = models.DateField(null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    preferred_username = models.CharField(max_length=255, blank=True, null=True)
    email_verified = models.NullBooleanField(default=False)

    phone_number = models.CharField(max_length=255, blank=True, null=True)
    phone_number_verified = models.NullBooleanField(default=False)

    address_locality = models.CharField(max_length=255, blank=True, null=True)
    address_country = models.CharField(max_length=255, blank=True, null=True)

    @classmethod
    def get_by_user(cls, user):
        return cls.objects.get(user=user)