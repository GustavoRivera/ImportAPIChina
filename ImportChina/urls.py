from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/', include('Apps.Catalogo.urls')),
    path('getapi/', include('Apps.GetAPI.urls')),
    
]
