from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]