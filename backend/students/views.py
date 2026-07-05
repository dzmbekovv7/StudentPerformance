from rest_framework.viewsets import ModelViewSet
from .models import Student, AcademicRecord, Prediction
from .serializers import StudentSerializer, AcademicRecordSerializer, PredictionSerializer
from accounts.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsTeacher
import joblib
from rest_framework.response import Response
from rest_framework.views import APIView
import numpy as np

predict_final_percentage_model = joblib.load("../machine_learning/models/final_percentage_prediction.pkl")
predict_pass_model = joblib.load("../machine_learning/models/pass_prediction.pkl")

class PredictFinalScoreAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def post(self, request, id):
        serializer = PredictionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        student = Student.objects.get(student_id=id)

        input_data = np.array([[
            data["Attendance_Percentage"],
            data["Study_Hours_Per_Day"],
            data["Math_Score"],
            data["Science_Score"],
            data["English_Score"],
            data["Previous_Year_Score"],
        ]])

        prediction_value = predict_final_percentage_model.predict(input_data)[0]

        prediction = Prediction.objects.create(
            student=student,
            teacher=request.user,
            input_data=data,
            predicted_final_percentage=prediction_value
        )

        return Response({
            "prediction_id": prediction.id,
            "predicted_final_percentage": prediction.predicted_final_percentage,
            "teacher_name": prediction.teacher.username,
        })

class PredictPassAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def post(self, request,id):
        serializer = PredictionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        student = Student.objects.get(student_id=id)
        input_data = np.array([[
            data["Attendance_Percentage"],
            data["Study_Hours_Per_Day"],
            data["Math_Score"],
            data["Science_Score"],
            data["English_Score"],
            data["Previous_Year_Score"],
        ]])


        prediction_value = predict_pass_model.predict(input_data)[0]

        prediction_value = bool(prediction_value)

        prediction = Prediction.objects.create(
            student=student,
            teacher=request.user,
            input_data=data,
            passed=prediction_value
        )

        return Response({
            "prediction_id": prediction.id,
            "passed": prediction.passed,
            "teacher_name": prediction.teacher.username
        })

class TeacherDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = Student.objects.all()

        result = []

        for student in students:
            predictions = Prediction.objects.filter(student=student).order_by("-created_at")

            latest = predictions.first()

            result.append({
                "student_id": student.student_id,
                "student_name": str(student),
                "latest_prediction": latest.predicted_final_percentage if latest else None,
                "total_predictions": predictions.count(),
                "last_updated": latest.created_at if latest else None
            })

        return Response(result)
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

class AcademicRecordViewSet(ModelViewSet):
    queryset = AcademicRecord.objects.all()
    serializer_class = AcademicRecordSerializer
    permission_classes = [IsAuthenticated, IsTeacher]
