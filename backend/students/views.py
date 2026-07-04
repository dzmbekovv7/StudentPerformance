from rest_framework.viewsets import ModelViewSet
from .models import Student, AcademicRecord
from .serializers import StudentSerializer, AcademicRecordSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsTeacher
import joblib
from rest_framework.response import Response
from rest_framework.views import APIView
import numpy as np

model = joblib.load("../machine_learning/models/final_percentage_prediction.pkl")

class PredictFinalScoreAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        input_data = np.array([[
            data["Attendance_Percentage"],
            data["Study_Hours_Per_Day"],
            data["Math_Score"],
            data["Science_Score"],
            data["English_Score"],
            data["Previous_Year_Score"],
        ]])

        prediction = model.predict(input_data)[0]

        return Response({"prediction": prediction})

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

class AcademicRecordViewSet(ModelViewSet):
    queryset = AcademicRecord.objects.all()
    serializer_class = AcademicRecordSerializer
    permission_classes = [IsAuthenticated, IsTeacher]
