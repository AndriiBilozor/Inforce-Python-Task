from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from restaurant.models import Restaurant  # Import the Restaurant model
from .models import Menu
from .serializers import MenuSerializer
from datetime import date


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_menu(request):
    if request.method == 'POST':

        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_day_menu(request):
    if request.method == 'GET':
        # Retrieve the current day's menu (simplified example)
        # You should implement your logic to query the menu for the current day
        # and return it in the response
        try:
            menus = Menu.objects.filter(date=date.today())
            serializer = MenuSerializer(menus, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Menu.DoesNotExist:
            return Response({'message': 'Menu for the current day is not available.'},
                            status = status.HTTP_404_NOT_FOUND)
