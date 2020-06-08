from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save 
from django.dispatch import receiver

class User(AbstractUser):
    email = models.EmailField()

    def logged_in(self):
        return self.last_login


class Profile(models.Model):

    TEAM_CHOICES = [
        ('IB', 'INBOUND'),
        ('OB', 'OUTBOUND'),
        ('WI', 'WALK IN'),
        ('FD', 'FOOD'),
        ('SM', 'SOCIAL MEDIA'),
        ('OT', 'OTHER'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.CharField(max_length=150, choices=TEAM_CHOICES, default='OT',)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars/', default='avatars/avatar.png')

    def __str__(self):
        return self.user.username


"""receivers to add a Profile for newly created users"""
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         Profile.objects.create(user=instance)

@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()