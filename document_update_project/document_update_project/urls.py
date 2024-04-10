# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('document_update.urls')),  # Include your app's URLs
    path('admin/', admin.site.urls),
]
