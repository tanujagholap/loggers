from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializers
from rest_framework.generics import ListCreateAPIView
from .models import Student
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentListApi(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

