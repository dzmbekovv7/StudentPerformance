from django.urls import path
from .views import CreateStudentAPIView, LoginAPIView, MeAPIView

urlpatterns = [
    path('register/', CreateStudentAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('me/', MeAPIView.as_view()),
]