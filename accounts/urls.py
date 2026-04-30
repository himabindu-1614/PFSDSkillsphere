from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('register/', views.register_view),
path('logout/', views.logout_view, name='logout'),
    path('login/', views.user_login, name='login'),
]