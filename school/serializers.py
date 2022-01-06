from rest_framework import serializers
from .models import School, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['email', 'first_name', 'last_name', 'gender', 'address', 'dob']

class SchoolSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = School
        fields = ['student','school_name', 'school_logo', 'school_motto', 'school_address', 'school_phone']

