from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_menu, name='upload-menu'),
    path('today/', views.get_current_day_menu, name='get-menu'),
]
