from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Job, Category, Location, Qualification, Company


class JobSerializer(serializers.ModelSerializer):

    location = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=True)
    qualification = serializers.StringRelatedField(many=True)
    applicants = serializers.StringRelatedField(many=True)
    company = serializers.StringRelatedField()

    class Meta:
        model = Job
        fields = ('__all__')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name',)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('name',)