from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views
from .views import *
from django.urls import path, include, re_path

app_name = 'accounts'

urlpatterns = [
	# path('sign-up/', RegistrationUserView.as_view(), name='sign-up'),
	path('login/', views.LoginView.as_view(template_name='rest_framework/login.html'), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
