from django.urls import re_path
from . import views

app_name = 'myapp'

urlpatterns = [
    re_path(r'^home/$', views.home_page, name='home'),
    re_path(r'^login/$', views.Login, name='login'),
    re_path(r'^menu/$', views.Menu, name='menu'),
    re_path(r'^news/$', views.News, name='news'),
    re_path(r'^dish/$', views.Dish, name='dish'),
    re_path(r'^contact/$', views.Contact, name='contact'),
    re_path(r'^admin/$', views.Admin, name='admin'),
    re_path(r'^about/$', views.About, name='about'),
]
