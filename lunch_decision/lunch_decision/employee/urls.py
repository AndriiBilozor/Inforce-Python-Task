from django.urls import path
from .views import create_employee, employee_authentication, show_all_employees

urlpatterns = [
    path('create/', create_employee, name='create-employee'),
    path('authenticate/', employee_authentication, name='employee-authentication'),
    path('all/', show_all_employees, name='show-all-employees')
]
