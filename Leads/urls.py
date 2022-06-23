from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeadListView.as_view(), name="lead-home"),
    path('details/<pk>/', views.LeadDetailView.as_view(), name="lead-details"),
    path('create/', views.LeadCreateView.as_view(), name="lead-create"),
    path('categories/', views.CategoryListView.as_view(), name="category-home"),
    path('categories/details/<pk>', views.CategoryDetailView.as_view(), name="category-details"),
    path('assign-agent/<pk>/', views.AssignAgentView.as_view(), name="lead-assign"),
    path('update/<pk>/', views.LeadUpdateView.as_view(), name="lead-update"),
    path('delete/<pk>/', views.LeadDeleteView.as_view(), name="lead-delete"),
]
