from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.datetime_safe import strftime
from autoslug import AutoSlugField
import datetime

from rest_framework.authtoken.models import Token


class MediaPath:
	def __init__(self, directory_name):
		super().__init__()
		self.directory_name = directory_name
		self.now = datetime.datetime.now()

	def directory_path_datatime(self, instance, filename):
		path_url = f'{instance.profile._meta.model_name}/{self.directory_name}'
		path_url += f'/user_{instance.profile.user.username}/%m/%d/%Y{filename}'
		return strftime(self.now, path_url)


class Gender(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = AutoSlugField(populate_from='name')

	def __str__(self):
		return self.name


class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	age = models.IntegerField(blank=True, null=True)
	date_of_birth = models.DateField(blank=True, null=True)
	slug = models.SlugField(blank=True)

	class HairColor(models.TextChoices):
		PREFER_NOT_ANSWER = 'Not Answer', _('Предпочитаю не отвечать')
		BLUE = 'Blue', _('Синий')
		BLACK = 'Black', _('Черный')
		WHITE = 'White', _('Белый')

	class EyeColors(models.TextChoices):
		PREFER_NOT_ANSWER = 'Not Answer', _('Предпочитаю не отвечать')
		BLUE = 'Blue', _('Синий')
		BLACK = 'Black', _('Черный')
		WHITE = 'White', _('Белый')

	eye_color = models.CharField(
		max_length=10,
		choices=EyeColors.choices,
		default=EyeColors.PREFER_NOT_ANSWER,
		db_index=True
	)
	hair_color = models.CharField(
		max_length=10,
		choices=HairColor.choices,
		db_index=True,
		default=HairColor.PREFER_NOT_ANSWER
	)
	gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
	height = models.PositiveIntegerField(blank=True, null=True)
	weight = models.PositiveIntegerField(blank=True, null=True)
	about_me = models.TextField(blank=True, null=True)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			pro = Profile(user=instance)
			pro.slug = slugify(instance.username)
			pro.save()

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

	@receiver(post_save, sender=User)
	def create_auth_token(sender, instance=None, created=False, **kwargs):
		if created:
			Token.objects.create(user=instance)

	def __str__(self):
		return f'{self.slug}-profile'


class Image(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images')
	image = ProcessedImageField(
		upload_to=MediaPath('avatars').directory_path_datatime,
	)
	is_main = models.BooleanField(default=False)



