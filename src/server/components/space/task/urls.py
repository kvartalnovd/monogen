from django.urls import path

from .views import Company

urlpatterns = [
	path('company', Company.as_view())
]