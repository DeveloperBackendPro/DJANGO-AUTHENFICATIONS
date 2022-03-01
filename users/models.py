from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

class User(AbstractUser):
    is_freelancer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='freelancer')
    phone = models.CharField(blank=True, max_length=20)
    skills = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)
    portofolio = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.user.username

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    company_name = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.user.username