# api/urls.py
from django.urls import path
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Shortener API",
        default_version='v1',
        description="The simple URL shortener.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kinlo443@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('v1/create/', views.create, name='create'),
    path('v1/<str:admin_url>/', views.list, name='list'),
    path('v1/<str:admin_url>/create/', views.create, name='create'),
    path('v1/<str:admin_url>/<str:short_url>/', views.info, name='info'),
    path('v1/<str:admin_url>/<str:short_url>/stats/', views.stats, name='stats'),
    path('v1/<str:admin_url>/<str:short_url>/update/', views.update, name='update'),
    path('v1/<str:admin_url>/<str:short_url>/delete/', views.delete, name='delete'),
]
