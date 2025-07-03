from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.stationary_list, name='stationary_list'),           # List all items
    path('add/', views.add_stationary, name='add_stationary'),         # Add new item
    path('update/<int:pk>/', views.update_stationary, name='update_stationary'), # Update item
    path('delete/<int:pk>/', views.delete_stationary, name='delete_stationary'), # Delete item
]