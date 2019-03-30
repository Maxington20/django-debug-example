from django.conf.urls import url
from AppTwo import views
from django.urls import path, re_path

urlpatterns = [
    path('',views.index, name="index"),
    path('help',views.help, name="help"),
    path('users',views.user,name='users'),
]