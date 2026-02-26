from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


User = get_user_model()
class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators = [UniqueValidator(queryset=User.objects.all())])
    password_1=serializers.CharField(required=True,write_only=True)
    password_2=serializers.CharField(required=True,write_only=True)
    class Meta:
        model = User
        fields = ('username','email','password_1','password_2','first_name','last_name')
        extra_kwargs = {
            'first_name': {'required':False},
            'last_name': {'required':False}
        }
    def validate(self,attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError('password_2 not match')
        return attrs
    def create(self,validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password_1'],
            first_name = validated_data.get('first_name',''),
            last_name = validated_data.get('last_name','')
        )
        return user



