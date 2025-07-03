from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.repair_list, name='repair_list'),
    path('add/', views.add_repair, name='add_repair'),
    path('update/<int:pk>/', views.update_repair, name='update_repair'),
    path('delete/<int:pk>/', views.delete_repair, name='delete_repair'),
]
