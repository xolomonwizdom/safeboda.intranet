from django.urls import path, include
from .views import RegistrationView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegistrationView.as_view(), name='register'),
]
