from django.urls import path, include

from Apps.GetAPI.views import *

urlpatterns= [
	path('', catalogoAPI.as_view(), name="catalogoAPI"),
]