from django.urls import path
from . import views

app_name = 'ktGuide'
urlpatterns = [
    path('index/', views.index, name='index')
]