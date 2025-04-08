from django.urls import path
from core_apps.accounts import views as UserViews
from . import views

urlpatterns = [
    # API root
    path('', views.api_root, name='api-root'),
    
    # User endpoints
    path('register/', UserViews.RegisterView.as_view(), name='user-register'),
]