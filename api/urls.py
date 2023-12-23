from django.urls import path
from .views import QuestionnairesAPIView

app_name = 'api'

urlpatterns = [
	path('questionnaires/',  QuestionnairesAPIView.as_view(), name='questionnaires-list')
]
