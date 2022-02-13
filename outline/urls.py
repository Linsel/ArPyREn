from django.urls import path
from django.contrib import admin
from . import views

# TEMPLATE TAGGING
app_name = 'outline'

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('tools/', views.import_tools, name='import_tools'),
    path('retouch/', views.retouch, name='retouch'),
    path('form_person/', views.form_person, name='form_person'),
    path('form_publication/', views.form_publication, name='form_publication'),
    path('logout/',views.user_logout,name='logout'),
    path('login/',views.user_login,name='login'),
    path('special/',views.special,name='special'),
]
