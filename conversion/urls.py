from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('text/', views.get_text),
    path('convert/', views.convert_image),
    path('image/', views.get_images),
]
