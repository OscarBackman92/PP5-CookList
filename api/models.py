from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100, unique=True)  # Title of the recipe, must be unique
    description = models.TextField()  # Detailed description of the recipe
    image = models.ImageField(upload_to='images/')  # Image field to upload recipe images
    ingredients = models.TextField()  # Ingredients required for the recipe
    instructions = models.TextField()  # Step-by-step instructions for preparing the recipe
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the recipe was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the recipe was last updated
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User who created the recipe
    preparation_time = models.PositiveIntegerField(help_text="Preparation time in minutes", default=0)  # Time needed to prepare the recipe
    servings = models.PositiveIntegerField(default=1)  # Number of servings the recipe yields

    def __str__(self):
        return self.title  # String representation of the recipe object
