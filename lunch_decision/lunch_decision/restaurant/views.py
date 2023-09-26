from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import RestaurantSerializer


@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated users for restaurant authentication
def restaurant_authentication(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate the user by email and password
        user = authenticate(request, username=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(token, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAdminUser])  # Allow only admin users to create a restaurant
def create_restaurant(request):
    if request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
