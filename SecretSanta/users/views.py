from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer

@api_view(['GET'])
def users_list(request):
    users = UserProfile.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    return Response({"users": serializer.data})