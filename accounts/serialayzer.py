from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.models import Profile


# class UserRegistrationSerializer(serializers.ModelSerializer):
#
# 	class Meta:
# 		model = User
# 		fields = ['id', 'username', 'email', 'password']
# 		extra_kwargs = {'password': {'write_only': True}}
#
# 	def create(self, validated_data):
# 		email = validated_data.get('email', None)
# 		if email is None:
# 			raise ValidationError({
# 				"email": "Enter a valid email address."
# 			})
# 		if User.objects.filter(email=email).exists():
# 			raise ValidationError({"email": 'Email already in use.'})
# 		user = User(
# 			email=validated_data['email'],
# 			username=validated_data['username'],
# 		)
# 		password = validated_data['password']
# 		user.set_password(password)
# 		user.save()
# 		return user
#
# 	def update(self, instance, validated_data):
# 		instance.email = validated_data.get('email', instance.email)
# 		instance.username = validated_data.get('username', instance.username)
# 		instance.save()
# 		return instance




