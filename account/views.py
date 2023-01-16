from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
# from rest_framework.serializers import UserSerializer


from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from drf_yasg.utils import swagger_auto_schema

from .serializers import RegisterUserSerializer
from .models import User
from .serializers import UserSerializer


class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=RegisterUserSerializer())
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Вы успешно зарегистрировались", status=201)

class DeleteUserView(APIView):
    def delete(self, request,email):
        user = get_object_or_404(User, email=email)
        print(user)
        print(request.user)
        if user.is_staff or user != request.user:
            return Response(status=403)
        user.delete()
        return Response(status=204) 

class UserListView(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer