from django.conf.urls import include, url
from . import views 

urlpatterns = [
    url(r'^home', views.home, name='learning_home'),
]
