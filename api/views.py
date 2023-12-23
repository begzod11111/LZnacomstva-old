from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer


# Create your views here.


class QuestionnairesAPIView(ListAPIView):
	permission_classes = [AllowAny]
	renderer_classes = [JSONRenderer]
	serializer_class = UserSerializer
	queryset = User.objects.all()
