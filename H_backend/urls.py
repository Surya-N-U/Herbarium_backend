from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'H_backend'

urlpatterns = [
    
    path('upload/', views.upload_image, name='upload_image'),
    # path('search/', views.search_images, name='search_images'),
    path('analytics/', views.analytics, name='analytics'),
    path('home/', views.home, name='home'),
    path('algae/', views.algae, name='algae'),
    path('gymnosperms/', views.gymnosperms, name='gymnosperms'),
    path('angiosperms/', views.angiosperms, name='angiosperms'),
    path('bryophytes/', views.bryophytes, name='bryophytes'),
    path('pteridophytes/', views.pteridophytes, name='pteridophytes'),
    path('monocotyledons/', views.monocotyledons, name='monocotyledons'),
    path('dicotyledons/', views.dicotyledons, name='dicotyledons'),
    path('search/', views.search, name='search'),
    path('edit/<int:plant_id>/', views.edit_plant, name='edit_plant'),
      
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
