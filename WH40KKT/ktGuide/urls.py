from django.urls import path
from . import views

app_name = 'ktGuide'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login/enter/', views.login_user, name='login_user'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('makeGuide/', views.make_guide, name='make_guide'),
    path('viewGuide/', views.view_guide, name='view_guide')
]