from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='../images/', default='../images/default_post_vlvmq3', blank=True
    )
    image_filter = models.CharField(max_length=255, choices=image_filter_choices, null=True, blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
