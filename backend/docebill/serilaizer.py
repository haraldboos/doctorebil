from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medical
        exclude=["date_joined","is_admin","is_staff","last_login","is_superuser","status","groups",'user_permissions']
        extra_kwargs={"password":{"write_only":True}}
    def create(self, validated_data):
        doctor = Medical.objects.create_dcophar(**validated_data)
        return doctor

        
