from django.urls import URLPattern, path

from .endpoint import auth_views, views


urlpatterns = [
	path('google/', auth_views.GoogleOauth.as_view()),
	path('', auth_views.GoogleLogin.as_view()),
]