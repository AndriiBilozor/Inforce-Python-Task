from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated users to create employees
def create_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated users for employee authentication
def employee_authentication(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(token, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_employees(request):
    """
    Returns a JSON response with QuerySet of all employees.
    """
    employees = Employee.objects.all()
    serialized_data = EmployeeSerializer(employees, many=True).data
    return Response({"employees": serialized_data})
