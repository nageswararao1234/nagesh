from rest_framework import serializers
from .models import CollegeUser


class TestSerializers(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    mobile = serializers.CharField()
    
    def validate_mobile(self, attrs):
        if not len(attrs) == 10:
            raise serializers.ValidationError("Mobile Number must has 10 digits.")
        if not attrs.isdigit():
            raise serializers.ValidationError("Mobile Number Must Digits Only.")
        if attrs[0] not in '9876':
            raise serializers.ValidationError("Mobile Number Has to starts with either of '9876' char.")
        return attrs
    

class CollegeUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CollegeUser
        fields = ["first_name", "last_name", "email", "dob"]
        read_only_fields = ["created_at", "modified_at"]
    
    def create(self, validated_data):
        return CollegeUser.objects.create(**validated_data)