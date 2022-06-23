from django.urls import path
from . import views

urlpatterns = [
    path('', views.AgentListView.as_view(), name="agent-home"),
    path('create/', views.AgentCreateView.as_view(), name="agent-create"),
    path('details/<pk>/', views.AgentDetailView.as_view(), name="agent-details"),
    path('update/<pk>/', views.AgentUpdateView.as_view(), name="agent-update"),
    path('delete/<pk>/', views.AgentDeleteView.as_view(), name="agent-delete"),
]
