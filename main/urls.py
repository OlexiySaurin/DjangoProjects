from django.urls import path
import hello.views
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name="home"),
    path('hello/', hello.views.helloworld, name="hello"),
]
