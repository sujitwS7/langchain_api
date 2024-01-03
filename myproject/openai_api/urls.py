from django.urls import path
from .views import create_session, generate_response

urlpatterns = [
    path('create_session/<str:user_id>/', create_session),
    path('generate_response/<str:user_id>/', generate_response),
]
