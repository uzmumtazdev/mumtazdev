from django.urls import path
from .views import list, detail, delete, Edit, post, search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', list, name='home'),
    path('post/<int:pk>/', detail, name='detail'),
    path('post/<int:pk>/delete/', delete, name='delete'),
    path('post/<int:pk>/edit/', Edit.as_view(), name='edit'),
    path('post/add/', post, name='add'),
    path('search/', search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
