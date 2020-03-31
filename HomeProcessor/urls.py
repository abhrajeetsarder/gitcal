from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('',views.HomeServer,name="home"),
    path('add', views.add, name='add'),
    path('home.html', views.HomeServer, name='home'),
    path('enter', views.enter, name='calculation'),

]
urlpatterns += staticfiles_urlpatterns()