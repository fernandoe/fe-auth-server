# -*- coding:utf-8 -*-
from fe_core.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from fe_auth.serializers import RegisterSerializer


@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        password = serializer.data['password']
        try:
            User.objects.get(email=email)
            data = {'email': 'E-mail já cadastro em nosso sistema.'}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            User.objects.create_user(email=email, password=password)
            return Response(data={}, status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    serializer = RegisterSerializer(data=request.data)
    return Response(data={})
