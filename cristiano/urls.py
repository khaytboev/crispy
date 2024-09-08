from django.urls import path
from cristiano import views


urlpatterns = [
    path('', views.signup, name='signup'),
    path('crispy/', views.crispy_signup, name='crispy_signup'),
]