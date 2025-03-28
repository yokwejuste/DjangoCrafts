from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin


class STUserManager(UserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)
    

class STUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = STUserManager()

    def is_verified(self):
        return self.is_verified

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"STUser(username={self.username}, is_verified={self.is_verified}, is_active={self.is_active})"
    
    class Meta:
        verbose_name = 'STUser'
        verbose_name_plural = 'STUsers'
        ordering = ['username']
        db_table = 'st_user'
        indexes = [
            models.Index(fields=['username'], name='username_idx'),
            models.Index(fields=['email'], name='email_idx'),
        ]
        unique_together = (('username', 'email'),)