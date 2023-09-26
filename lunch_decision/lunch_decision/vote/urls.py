from django.urls import path
from .views import vote, get_results

urlpatterns = [
    path('make/', vote, name='make-a-vote'),
    path('result/', get_results, name='get-results'),
]
