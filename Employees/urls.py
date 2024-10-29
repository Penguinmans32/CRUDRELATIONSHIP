from django.urls import path
from . import views

urlpatterns = [
    path('job_titles/', views.job_title_list, name='job_title_list'),
    path('job_titles/create/', views.job_title_create, name='job_title_create'),
    path('job_titles/update/<int:pk>/', views.job_title_update, name='job_title_update'),
    path('job_titles/delete/<int:pk>/', views.job_title_delete, name='job_title_delete'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/update/<int:pk>/', views.employee_update, name='employee_update'),
    path('employees/delete/<int:pk>/', views.employee_delete, name='employee_delete'),

    path('employment_terms/', views.employment_terms_list, name='employment_terms_list'),
    path('employment_terms/create/', views.employment_terms_create, name='employment_terms_create'),
    path('employment_terms/update/<int:pk>/', views.employment_terms_update, name='employment_terms_update'),
    path('employment_terms/delete/<int:pk>/', views.employment_terms_delete, name='employment_terms_delete'),
]
