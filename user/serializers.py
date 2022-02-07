from rest_framework import serializers
from .models import user, reports

class userReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['user']
