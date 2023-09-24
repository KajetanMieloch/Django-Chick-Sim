
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('henHouse/', include('henHouse.urls')),
    path('buildings/', include('buildings.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
