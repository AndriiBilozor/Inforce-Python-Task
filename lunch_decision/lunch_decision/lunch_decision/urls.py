"""lunch_decision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint for obtaining JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint for refreshing JWT token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Endpoint for verifying JWT token
    path('employee/', include('employee.urls')),  # Include employee app URLs
    path('restaurant/', include('restaurant.urls')),  # Include restaurant app URLs
    path('menu/', include('menu.urls')),  # Include restaurant app URLs
    path('vote/', include('vote.urls')),  # Include restaurant app URLs
]
