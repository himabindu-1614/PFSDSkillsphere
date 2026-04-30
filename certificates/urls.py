from django.urls import path
from . import views

urlpatterns = [

path(
'',
views.certificates,
name='certificates'
),

path(
'dashboard/',
views.dashboard,
name='dashboard'
),

path(
'add/',
views.add_certificate,
name='add_certificate'
),

path(
'profile/',
views.profile,
name='profile'
),

path(
'view/<int:pk>/',
views.preview_certificate,
name='preview_certificate'
),

path(
'edit/<int:pk>/',
views.edit_certificate,
name='edit_certificate'
),

path(
'delete/<int:pk>/',
views.delete_certificate,
name='delete_certificate'
),

]