from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.core.mail import send_mail
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, username=None, password=None):
        if not email:
            raise ValueError('A user must have an email address.')

        if not username:
            raise ValueError('Please provide a username.')

        if not password:
            raise ValueError('Please provide a password.')

        user = self.model(
            email=self.normalize_email(email),
            username=username

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username=username, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, blank=False, max_length=250, verbose_name='email address')
    username = models.CharField(max_length=30, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email, ])

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)