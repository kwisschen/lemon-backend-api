from django.urls import path
from . import views
from djoser.views import UserViewSet

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),  # List all registered users
]
