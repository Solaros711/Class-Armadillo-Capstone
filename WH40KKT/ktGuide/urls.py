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
    path('view_guide/<int:guide_id>/', views.view_guide, name='view_guide'),
    path('get_units/', views.get_units, name='get_units'),
    path('get_unit_stuff/', views.get_unit_stuff, name='get_unit_stuff'),
    path('get_presentable/', views.get_presentable, name='get_presentable'),
    path('submit_guide/', views.submit_guide, name='submit_guide'),
    path('submit_comment/', views.submit_comment, name='submit_comment')
]