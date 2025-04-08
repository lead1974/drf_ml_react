from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Base API Endpoint
    path('api/v1/', include('core_apps.api.urls')),

    # Redirect root to API
    path('', RedirectView.as_view(url='api/v1/', permanent=False)),
]