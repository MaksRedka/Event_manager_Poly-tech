from django.urls import path
from .views import EventListApiView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/', EventListApiView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]