from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='Film Application Rest API',
        default_version='v1',
        description='Swagger docs for Rest API',
        contact=openapi.Contact('James Bond <bond9171769@gmail.com>'),
    ),
    public=True,
    permission_classes=[AllowAny,]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('film.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc docs'),
]
