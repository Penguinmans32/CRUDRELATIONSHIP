# MainProject/urls.py
from django.contrib import admin
from django.urls import path, include
from Employees import views  # Capitalized as 'Employees'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('Employees.urls')),  # Ensure 'Employees' is capitalized
    path('', views.index, name='index'),
]
