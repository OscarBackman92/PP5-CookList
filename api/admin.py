from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'owner__username')
    list_filter = ('created_at',)

admin.site.register(Recipe, RecipeAdmin)
