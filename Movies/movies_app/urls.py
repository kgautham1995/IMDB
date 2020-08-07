from django.contrib import admin
from django.urls import path
from movies_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addmovie/',views.addmovie,name="addmovie"),
    path('savemovie/',views.savemovie,name="savemovie"),
]
