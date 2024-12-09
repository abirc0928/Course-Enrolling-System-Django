from django.shortcuts import render
from rest_framework.views import APIView, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegistrationView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = User.objects.create_user(username=username, password=password)

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status":"success" ,
                'user_id' :user.id , 
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
    
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        tokens = response.data 

        response.set_cookie(
            key="refresh_token",
            value=tokens["refresh"],
            httponly=True,
           
        )

        response.set_cookie(
            key="access_token",
            value=tokens["access"],
            httponly=True,
            
        )

        print("tokens",tokens)
        return response

class LogoutView(APIView):
    def post(self, request):
        # Create a response
        response = Response({"success": "Logged out successfully"})
 
        # Delete the access and refresh token cookies
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response