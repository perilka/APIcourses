from rest_framework import serializers
from .models import University, Course, UniversityCourse


class UniversityCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityCourse
        read_only_fields = ["id"]
        fields = [
            'id',
            'university',
            'course',
            'semester',
            'duration_weeks'
        ]

class UniversitySerializer(serializers.ModelSerializer):
    courses = UniversityCourseSerializer(many=True, read_only=True)

    class Meta:
        model = University
        read_only_fields = ["id"]
        fields = [
            'id',
            'name',
            'country',
            'courses'
        ]

class CourseSerializer(serializers.ModelSerializer):
    details = UniversityCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        read_only_fields = ["id"]
        fields = [
            'id',
            'title',
            'description',
            'details'
        ]