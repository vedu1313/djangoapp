from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('course',views.course, name='course'),
    path('contact',views.contacts,name='contact'),
    path('about',views.about,name='about'),
]