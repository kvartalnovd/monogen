from django.core.validators import FileExtensionValidator
from django.db import models

from components.common.oauth.services.auth_user import AuthUserService


class AuthUser(models.Model):
    """User model on the platform"""
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(upload_to=AuthUserService.get_path_upload_avatar,
                               blank=True,
                               null=True,
                               validators=[FileExtensionValidator(allowed_extensions=['jpg']),
                                           AuthUserService.validate_avatar_file_size])

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.email


class Follower(models.Model):
    """ Follower model """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='subscriber')

    def __str__(self):
        return f'{self.subscriber} is subscribed to {self.user}'


class UserSocialLink(models.Model):
    """ Links model to the user's social networks """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='social_links')
    link = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.user}'
