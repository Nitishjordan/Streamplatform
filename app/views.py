from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import StreamPlatform, WatchList
from .serializers import StreamPlatformSerializer, UserSignupSerializer, UserLoginSerializer, WatchListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework import status


@api_view(['GET'])
@swagger_auto_schema(
    operations_summary="My summaries",
    operations_description="My summaries description",
    response = {200:"Success"}


)
def movie_list(request):
    movie_list = WatchList.objects.all()
    serialized = WatchListSerializer(movie_list,many= True)
    return Response(serialized.data)

@api_view(['GET'])
def movie_detail(request,pk):
    movie_detail = WatchList.objects.get(pk=pk)
    serialized = WatchListSerializer(movie_detail)
    return Response(serialized.data,safe = False)

@api_view(['GET'])
def stream_list(request):
    streamDetails = StreamPlatform.objects.all()
    serialized = StreamPlatformSerializer(streamDetails,many= True)
    return Response(serialized.data, safe= False)

@api_view(['GET'])
def stream_detail(request,pk):
    streamDetails = StreamPlatform.objects.get(pk=pk)
    serialized = StreamPlatformSerializer(streamDetails)
    return Response(serialized.data, safe= False)




class SignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data= request.data)
        if serializer.is_valid():
            username = serializer.validate_data['username']
            password = serializer.validate_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZEDITIBLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
