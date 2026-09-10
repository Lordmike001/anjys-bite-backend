from django.shortcuts import render
from rest_framework import generics, status
from authentication.serializers import SignUpSerializer, LoginSerializer
from rest_framework.response import Response

# from authentication.models import User
# Create your views here.


class SignUpViews(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email").lower()
        password = serializer.validated_data.get("password")
        phone_number = serializer.validated_data.get("phone_number")
        address = serializer.validated_data.get("address")
        bvn = serializer.validated_data.get("bvn")
        dob = serializer.validated_data.get("dob")
        return Response(data={"message": "Ok!"}, status=status.HTTP_201_CREATED)


class LoginViews(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        return Response(data={'message': 'Successful'}, status=status.HTTP_202_ACCEPTED)