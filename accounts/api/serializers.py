# from rest_framework import serializers
# from accounts.models import CustomUser
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password


# class UserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(
#             required=True,
#             validators=[UniqueValidator(queryset=CustomUser.objects.all())]
#             )
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password', 'password2', )

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})
#         return attrs

#     def create(self, validated_data):
#         user = CustomUser.objects.create(
#             username=validated_data['username'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

























from rest_framework import serializers

from accounts.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
				'password': {'write_only': True},
		}

    def	save(self):
        account = CustomUser(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account

