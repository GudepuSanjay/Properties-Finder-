"""
URL configuration for UnderstandingProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from UnderstandingProject import views
import properties_bookings
from buying_properties import urls
from rent_properties import urls
from agents_profiles import urls
# from properties import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    # path('home/',include('properties.urls')),
    path('',include('properties.urls')),
    path('',include('properties_bookings.urls')),
    path('',include('buying_properties.urls')),
    path('',include('rent_properties.urls')),
    path('',include('agents_profiles.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
