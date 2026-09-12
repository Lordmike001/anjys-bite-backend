from django.shortcuts import render
from rest_framework import generics, status
from authentication.serializers import SignUpSerializer, LoginSerializers
from rest_framework.response import Response
from authentication.models import User

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
        # return Response(data={"message": "Ok!"}, status=status.HTTP_201_CREATED)
        email_exists = User.objects.filter(email=email).first()
        if email_exists:
            return Response(
                data={"message": "Email already Exist!!"},
                status=status.HTTP_226_IM_USED,
            )
        user = User.objects.create(
            email=email,
            phone_number=phone_number,
            address=address,
            bvn=bvn,
            dob=dob,
            # account_type = account_type
        )

        user.set_password(password)
        user.save()

        return Response(
            data={"Message": "Account Successfully Created"},
            status=status.HTTP_201_CREATED,
        )


class LoginViews(generics.GenericAPIView):
    serializer_class = LoginSerializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        return Response(data={"message": "Successful"}, status=status.HTTP_202_ACCEPTED)
        email_exists = User.objects.filter(email=email).first()

        if not email_exists:
            return Response(
                data={"Message": "Invalid Credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        user = authenticate(email=email, password=password)
        if not user:
            return Response(
                data={"Message": "Invalid Credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            data={
                "id": str[user.id],
                "email": str[user.email],
                "is_admin": user.is_staff,
                "phone_number": user.phone_number,
            }
        )
