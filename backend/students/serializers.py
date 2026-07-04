from rest_framework import serializers
from .models import Student, AcademicRecord

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class AcademicRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicRecord
        fields = "__all__"