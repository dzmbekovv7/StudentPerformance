from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .permissions import IsTeacher
from rest_framework_simplejwt.tokens import RefreshToken

class CreateStudentAPIView(APIView):
    permission_classes = [IsTeacher]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'username': user.username, "message": "Student created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user= serializer.validated_data["user"]
        user_data = UserSerializer(user).data
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": user_data
            },
            status = status.HTTP_200_OK

        )

class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)