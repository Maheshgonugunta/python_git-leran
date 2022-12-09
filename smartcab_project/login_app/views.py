from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import loginSerializer
from.models import login
from rest_framework.authentication import TokenAuthentication


# Class based view to Get User Details using Token Authentication
class loginDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def post(self,request,*args,**kwargs):
 #   print(request.data.username)
    print(request.data)
    print(type(request.data))
    user = login.objects.get(username=request.POST.get('username'))

    serializer = loginSerializer(user)
    return Response(serializer.data)

#Class based view to register user
#class RegisterUserAPIView(generics.CreateAPIView):
#  permission_classes = (AllowAny,)
  #serializer_class = RegisterSerializer
