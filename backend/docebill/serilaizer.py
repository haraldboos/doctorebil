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
class DesiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desies
        fields = '__all__'

class MedicinSerializer(serializers.ModelSerializer):
    class Meta:
        model=medicine
        exclude=['adddate','status']
class SubdiseSerializer(serializers.ModelSerializer):
    maindesis = DesiesSerializer()
    class Meta:
        model=subdesies
        fields='__all__'

class CollectionSerilazer(serializers.ModelSerializer):
    subdesies_id= serializers.PrimaryKeyRelatedField(queryset=subdesies.objects.all(),source='subdesies')
    medicine_id = serializers.PrimaryKeyRelatedField(queryset=medicine.objects.all(),source='medicine')
    class Meta:
        model=collection
        fields=['subdesies_id','medicine_id','days', 'note']

class Billserilazation(serializers.ModelSerializer):
        coll_id = serializers.PrimaryKeyRelatedField(queryset=collection.objects.all(),source='medicine')
        doc_id =serializers.PrimaryKeyRelatedField(queryset=Medical.objects.all(),source='billdoc')
        class Meta:
            model=Bill
            fields='__all__'

        # pass

