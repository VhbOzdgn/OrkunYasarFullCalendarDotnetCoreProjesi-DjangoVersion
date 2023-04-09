from django.urls import path
from .views import register_view, logout_view, login_view

urlpatterns = [
    path('login', view=login_view, name='login'),
    path('register', view=register_view, name='register'),
    path('logout', view=logout_view, name='logout'),
]
