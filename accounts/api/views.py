


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from accounts.api.serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny


@api_view(['POST', ])
@permission_classes([AllowAny])

def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
		else:
			data = serializer.errors
		return Response(data)





# class SignUpView():
#     permission_classes = (AllowAny,)
#     @api_view(['POST', ])
#     def registration_view(self,request):
#         if request.method == 'POST':
#             serializer = RegistrationSerializer(data=request.data)
#             data = {}
#             if serializer.is_valid():
#                 account = serializer.save()
#                 data['response'] = 'successfully registered new user.'
#                 data['email'] = account.email
#                 data['username'] = account.username
#             else:
#                 data = serializer.errors
#             return Response(data)











# import requests
# from rest_framework import status
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from accounts.models import CustomUser
# from .serializers import UserSerializer
# from rest_framework.permissions import AllowAny


# class SignUpView(APIView):
#     permission_classes = (AllowAny,)
#     def post(self, request):
#         data = request.data
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










