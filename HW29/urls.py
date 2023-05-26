import ads.views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from HW29 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ad/', include('ads.urls.ad')),
    path('selection/', include('ads.urls.selection')),
    path('cat/', include('ads.urls.cat')),
    path('user/', include('users.urls')),
    path('', ads.views.home),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

