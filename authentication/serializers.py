from rest_framework import serializers
from authentication.models import ACCOUNT_TYPE

class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    fullname = serializers.CharField(max_length=255)
    password = serializers.CharField()
    phone = serializers.CharField()
    account_type = serializers.ChoiceField(choices=[x[0] for x in ACCOUNT_TYPE], default=ACCOUNT_TYPE[0][0])
    address = serializers.CharField()
    dob = serializers.DateField()
    bvn = serializers.CharField()

    def validate(self, attrs):
        email = attrs["email"]
        if not email.endswith("anjy.com"):
            raise serializers.ValidationError("Email must end with anjy.com")

        phone = attrs["phone"]
        if not phone.startswith("+234"):
            raise serializers.ValidationError("Phone number must start with +234")

        if len(phone) != 14:
            raise serializers.ValidationError(
                "Phone number must be exactly 14 digits including '+' symbol "
            )
        try:
            int(phone[1:])
        except:
            raise serializers.ValidationError("Phone number must be digits only")

        bvn = attrs["bvn"]
        if not bvn.startswith("2"):
            raise serializers.ValidationError("BVN must start with 2")
        if len(bvn) != 11:
            raise serializers.ValidationError("BVN must be exactly 11 characters")
        try:
            int(bvn)
        except:
            raise serializers.ValidationError("BVN must be digits only")

        password = attrs["password"]
        if len(password) < 8:
            raise serializers.ValidationError(
                "Password must not be less than 8 characters"
            )
        return attrs


class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
