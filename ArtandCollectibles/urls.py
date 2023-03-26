from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'ArtandCollectibles Dashboard'
admin.site.site_title = 'ArtandCollectibles Admin Portal'
admin.site.index_title ='Welcome to ArtandCollectibles'

urlpatterns = [
    path('',include('art.urls')),
    path('admin/', admin.site.urls),
    path('captcha/',include('captcha.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   

