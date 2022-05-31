from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

app_name = 'userposts'

schema_view = get_schema_view(
    openapi.Info(
        title="AMCEF post Microservice API",
        default_version='v1',
        description="A simple RESTful API for basic CRUD operations w/ posts and without authentication.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hriadel@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include_docs_urls(title='AMCEF post Microservice API')),
    path('docs/', include_docs_urls(title='AMCEF post Microservice API')),
    path('amcefapi/', include('userposts.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

]
