from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import Prefetch
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from accounts.models import Profile, Image
# from accounts.serialayzer import UserRegistrationSerializer

# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })


# class RegistrationUserView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegistrationSerializer
#     permission_classes = [AllowAny]
#
#     def post(self, request, *args, **kwargs):
#
#         serializer = UserRegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data['response'] = True
#             return Response(data, status=status.HTTP_200_OK)
#         else:
#             data = serializer.errors
#             return Response(data)

