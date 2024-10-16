from rest_framework import serializers
from .models import Recipe
from likes.models import Like


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='author.username')  # Change 'owner' to 'author'
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')  # Change 'owner' to 'author'
    profile_image = serializers.ReadOnlyField(source='author.profile.image.url')  # Change 'owner' to 'author'
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author  # Change 'owner' to 'author'

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, recipe=obj).first()  # Change 'post' to 'recipe'
            return like.id if like else None
        return None

    class Meta:
        model = Recipe
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 
            'profile_image', 'created_at', 'updated_at', 
            'title', 'description', 'image', 'ingredients', 
            'instructions', 'preparation_time', 'servings',
            'like_id', 'likes_count', 'comments_count',
        ]
