from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]

handler404 = views.handler404