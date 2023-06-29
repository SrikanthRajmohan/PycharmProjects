# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('stock_data.urls', namespace='stock_data')),
# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock_data/', include('stock_data.urls', namespace='stock_data')),
]