from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from H_backend import views

urlpatterns = [
    path('admin/', views.custom_admin_dashboard, name='custom_admin_dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('H_backend.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
