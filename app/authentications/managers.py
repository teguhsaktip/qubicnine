import logging
from typing import Optional

from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Model, Q
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number: str, first_name: str, password: str, **extra_fields) -> Model:
        """
        Creates and saves a User with the given and password

        Arguments:
            first_name (str): First name of user
            password (str): Raw password of user
        """
        if not phone_number:
            raise ValueError(_('The given phone number must be set.'))
        if not first_name:
            raise ValueError(_('The given first name must be set.'))
        if not password:
            raise ValueError(_('The given password must be set.'))

        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number: str, first_name: str,  password: str, **extra_fields) -> Model:
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, first_name, password, **extra_fields)

    def create_superuser(self, phone_number: str, first_name: str, password: str, **extra_fields) -> Model:
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(phone_number, first_name, password, **extra_fields)

    def get_user(self, phone_number: str = None, email: str = None) -> Optional[Model]:
        """
        Get user by phone number or email

        Returns:
            User: User model if any or None
        """
        queryset = self.get_queryset()
        try:
            queryset = queryset.get(
                Q(phone_number=phone_number)
                | Q(email=email)
            )
        except Exception as e:
            logging.exception(e)
            queryset = None
        finally:
            return queryset
