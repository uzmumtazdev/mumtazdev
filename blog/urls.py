from django.urls import path
from .views import list, detail, delete, Edit, post, search

urlpatterns = [
    path('', list, name='home'),
    path('post/<int:pk>/', detail, name='detail'),
    path('post/<int:pk>/delete/', delete, name='delete'),
    path('post/<int:pk>/edit/', Edit.as_view(), name='edit'),
    path('post/add/', post, name='add'),
    path('search/', search, name='search'),
]
