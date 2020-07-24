from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Collections


class CollectionsSerializer(serializers.ModelSerializer):
    movies = serializers.ListField(child=serializers.UUIDField(format='hex_verbose', required=False), required=False)

    class Meta:
        model = Collections
        fields = ['title', 'description', 'movies']


    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        else:
            raise serializers.ValidationError
        instance = Collections.objects.create(owner=user, **validated_data)
        return instance

