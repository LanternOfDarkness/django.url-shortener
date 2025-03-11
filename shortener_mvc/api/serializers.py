from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['original_url', 'short_code', 'admin_token', 'created_at', 'updated_at', 'access_count']
