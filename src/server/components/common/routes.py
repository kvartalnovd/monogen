from django.urls import path, include

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="monogen",
        default_version='v1',
        description="application for students based on Django 4.0 & Django REST Framework",
        contact=openapi.Contact(url="https://t.me/kvartalnovd")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('components.common.oauth.urls'))
]
