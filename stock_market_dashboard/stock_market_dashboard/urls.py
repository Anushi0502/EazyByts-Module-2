from django.contrib import admin
from django.urls import path, include
from stocks.views import dashboard  # Import the dashboard view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),  # Redirect root URL to dashboard
    path('api/', include('stocks.urls')),  # Include the stocks app URLs
]
