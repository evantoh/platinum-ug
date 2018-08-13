from django.urls import path

from . import views

urlpatterns = [
    path('data/', views.premium_users, name='premium_users'),
    path('getcsv/', views.get_csv, name='get_csv'),
    path('premierdemands_report/', views.premierdemands_report, name='demand_reports'),
    path('journal_entry/', views.journal_entry, name='journals'),
]