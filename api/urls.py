from django.urls import path
# after
from . import views

urlpatterns = [
    path('api/register/', views.register, name='register'),
]
