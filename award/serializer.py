from rest_framework import serializers
from .models import *

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('user', 'rate')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('cover', 'project_name', 'location', 'profile', 'pub_date')