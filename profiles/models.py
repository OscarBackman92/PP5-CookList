from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    bio = models.TextField(blank=True)
    dietary_preferences = models.CharField(max_length=100, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_ylwpgw'
    )
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
