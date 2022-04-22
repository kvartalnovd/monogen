from django.urls import path

from .endpoint import auth_views, views


urlpatterns = [
	path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
	path('google/', auth_views.GoogleOauth.as_view()),
	path('', auth_views.GoogleLogin.as_view()),
]
