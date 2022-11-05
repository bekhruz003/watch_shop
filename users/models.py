from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import PhoneValidator
from django.utils.translation import gettext_lazy as _


class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=13, validators=[PhoneValidator()], unique=True)
    country = models.CharField(max_length=125, null=True, blank=True, verbose_name=_('country'))
    city_of_residence = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('address'))
    city_of_residence2 = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('address2'))
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('city'))
    district = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('district'))
    zip_code = models.CharField(max_length=6, null=True, blank=True, verbose_name=_('zip_code'))

    USERNAME_FIELD = 'phone_number'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

# class ProfileModel(models.Model):
#     user = models.OneToOneField(UserModel,
#                                 on_delete=models.CASCADE, verbose_name=_('user'))
#     country = models.CharField(max_length=125, null=True, blank=True, verbose_name=_('country'))
#     address1 = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('address1'))
#     address2 = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('address2'))
#     city = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('city'))
#     district = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('district'))
#     zip_code = models.CharField(max_length=6, null=True, blank=True, verbose_name=_('zip_code'))
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
#
#     class Meta:
#         verbose_name = 'profile'
#         verbose_name_plural = 'profiles'
