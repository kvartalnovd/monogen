"""
monogen URL Configuration

"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('components.common.routes')),
    path('', include('components.common.oauth.urls')),
    path('space', include('components.space.task.urls')),
]
