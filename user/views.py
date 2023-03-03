from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    # para q el pass esté hasheado en el json
    def perform_create(self, serializer):
        # el valor q estaba en [] es el name del input
        serializer.save(password=make_password(serializer.validated_data['password']))