from rest_framework.viewsets import ModelViewSet
from .models import Student, AcademicRecord
from .serializers import StudentSerializer, AcademicRecordSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsTeacher

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

class AcademicRecordViewSet(ModelViewSet):
    queryset = AcademicRecord.objects.all()
    serializer_class = AcademicRecordSerializer
    permission_classes = [IsAuthenticated, IsTeacher]
