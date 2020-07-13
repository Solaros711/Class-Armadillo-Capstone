from django.urls import path
from . import views

app_name = 'ktGuide'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('register/', views.register, name='register'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('makeGuide/', views.make_guide, name='make_guide'),
    path('viewGuide/', views.view_guide, name='view_guide'),
    path('get_units/', views.get_units, name='get_units'),
    path('get_unit_stuff/', views.get_unit_stuff, name='get_unit_stuff'),
    path('get_presentable/', views.get_presentable, name='get_presentable')
]