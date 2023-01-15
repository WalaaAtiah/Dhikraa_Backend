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
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['birthday']=account.birthday
            data['phone_number']=account.phone_number
            data['location']=account.location

        else:
            data = serializer.errors
        return Response(data)



