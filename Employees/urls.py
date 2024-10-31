# Employees/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Job Titles URLs
    path('job_titles/', views.job_title_list, name='job_title_list'),
    path('job_titles/create/', views.job_title_create, name='job_title_create'),
    path('job_titles/update/<int:pk>/', views.job_title_update, name='job_title_update'),
    path('job_titles/delete/<int:pk>/', views.job_title_delete, name='job_title_delete'),

    # Employee URLs
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/update/<int:pk>/', views.employee_update, name='employee_update'),
    path('employees/delete/<int:pk>/', views.employee_delete, name='employee_delete'),

    # Employment Terms URLs
    path('employment_terms/', views.employment_terms_list, name='employment_terms_list'),
    path('employment_terms/create/', views.employment_terms_create, name='employment_terms_create'),
    path('employment_terms/update/<int:pk>/', views.employment_terms_update, name='employment_terms_update'),
    path('employment_terms/delete/<int:pk>/', views.employment_terms_delete, name='employment_terms_delete'),

    # Department URLs
    path('departments/', views.department_list, name='department_list'),
    path('departments/new/', views.department_create, name='department_create'),
    path('departments/<int:pk>/edit/', views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),

    # Department History URLs
    path('department_history/', views.department_history_list, name='department_history_list'),
    path('department_history/new/', views.department_history_create, name='department_history_create'),
    path('department_history/<int:pk>/edit/', views.department_history_update, name='department_history_update'),
    path('department_history/<int:pk>/delete/', views.department_history_delete, name='department_history_delete'),
]
