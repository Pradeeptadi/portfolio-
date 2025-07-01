from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import homepage  # Only if homepage view is defined in this folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('projects/', include('project.urls')),  # Include the project app URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
