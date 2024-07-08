from django.urls import re_path
from . import views
from django.conf import settings 
from django.conf.urls.static import static


app_name = 'myapp'

urlpatterns = [
    re_path(r'^home/$', views.home_page, name='home'),
    re_path(r'^login/$', views.Login, name='login'),
    re_path(r'menu/', views.Menu, name='menu'),
    re_path(r'^news/$', views.News, name='news'),
    re_path(r'^dish/$', views.Dish, name='dish'),
    re_path(r'^contact/$', views.Contact, name='contact'),
    re_path(r'^admin/$', views.Admin, name='admin'),
    re_path(r'^about/$', views.About, name='about'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^makeorder/$', views.makeorder, name='makeorder'),
    re_path(r'^notification/$', views.notification, name='notification'),
    re_path(r'get_item_details/$', views.get_item_details, name='get_item_details'),]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
