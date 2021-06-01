from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_auth, name=' login_auth'),

]
