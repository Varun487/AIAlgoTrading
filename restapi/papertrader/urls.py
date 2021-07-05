from django.urls import path
from . import views

urlpatterns = [
    path('<slug>/', views.api_index, name='api_index'),
]
