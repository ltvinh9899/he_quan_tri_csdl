from django.urls import path
from . import views

app_name = 'user_seeking'
urlpatterns = [
    path('', views.index,name = 'user_seeking'),
]