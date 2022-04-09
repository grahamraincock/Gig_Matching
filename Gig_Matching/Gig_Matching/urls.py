"""
Definition of urls for Gig_Matching.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('newproject/', views.newproject, name='newproject'),
    path('myprojects/', views.myprojects, name='myprojects'),
    path('viewprojects/', views.viewprojects, name='viewprojects'),
    path('contactapp/<Account_ID>', views.contactapp, name='contactapp'),
    path('viewapplicants/<Project_ID>', views.viewapplicants, name='viewapplicants'),
    path('application/<Project_ID>', views.application, name='application'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
