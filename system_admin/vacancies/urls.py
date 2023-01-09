from django.urls import path
from django.conf.urls.static import static

from system_admin import settings
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('demand/', demand),
    path('geography/', geography),
    path('skills/', skills),
    path('recent/', recent)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
