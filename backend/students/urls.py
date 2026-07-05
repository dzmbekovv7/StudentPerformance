from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    AcademicRecordViewSet,
    StudentViewSet,
    PredictFinalScoreAPIView,
    PredictPassAPIView,
    TeacherDashboardAPIView
)

router = DefaultRouter()

router.register("students", StudentViewSet, basename="student")
router.register("academic-records", AcademicRecordViewSet, basename="academic-record")


urlpatterns = [
    path("", include(router.urls)),  # 👈 ViewSets go here

    path(
        "predict/<int:id>/final-score/",
        PredictFinalScoreAPIView.as_view(),
        name="predict-final-score"
    ),

    path(
        "predict/<int:id>/pass/",
        PredictPassAPIView.as_view(),
        name="predict-pass"
    ),

    path(
        "dashboard/",
        TeacherDashboardAPIView.as_view(),
        name="teacher-dashboard"
    )
]