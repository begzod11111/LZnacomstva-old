from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ('slug', 'age', 'about_me', 'gender')


class UserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer(many=False, read_only=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'profile')



