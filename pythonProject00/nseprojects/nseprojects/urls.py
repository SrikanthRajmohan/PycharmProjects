"""
URL configuration for nseprojects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
import datetime

from nseprojects.nsecodes.views import bhavcopy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bhavcopy/', bhavcopy, name='bhavcopy'),
]


# Set the NSE date
nse_date = datetime.date(2023, 6, 23)

# Set the NSE URL
#nse_url = "https://example.com/data"

# Use the NSE date and URL in your code
print("NSE Date:", nse_date)
#print("NSE URL:", nse_url)