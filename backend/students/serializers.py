from rest_framework import serializers
from .models import Student, AcademicRecord, Prediction

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class AcademicRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicRecord
        fields = "__all__"

class PredictionSerializer(serializers.Serializer):
    Attendance_Percentage = serializers.FloatField()
    Study_Hours_Per_Day = serializers.FloatField()
    Math_Score = serializers.FloatField()
    Science_Score = serializers.FloatField()
    English_Score = serializers.FloatField()
    Previous_Year_Score = serializers.FloatField()

