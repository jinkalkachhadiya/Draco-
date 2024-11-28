from django.urls import path
from DRApps.web.views import *
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('search/', views.search_anime, name='search_anime'),
    path('search_manga/', views.search_manga, name='search_manga'),

]
