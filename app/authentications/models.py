from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from authentications.managers import UserManager
from qubicnine.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone_number = PhoneNumberField(
        _('phone number'),
        unique=True,
        help_text=_('Phone number of user')
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
        help_text=_('Email of user'),
    )
    first_name = models.CharField(
        _('first name'),
        max_length=32,
        help_text=_('First name of user'),
    )
    last_name = models.CharField(
        _('last name'),
        null=True,
        blank=True,
        max_length=32,
        help_text=_('Last name of user'),
    )
    is_staff = models.BooleanField(
        _('is_staff'),
        default=False,
        help_text=_('Staff for django admin')
    )

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return '{} {}'.format(self.first_name, self.email)

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')