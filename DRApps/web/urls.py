# web/urls.py
from django.urls import path
from . import views
from DRApps.user.views import *

urlpatterns = [
    path('home/', views.manga_list, name='manga_list'),
    path('manga/<int:manga_id>/', views.manga_detail, name='manga_detail'),
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
    path('chapter/pdf/<int:chapter_id>/', views.chapter_pdf, name='chapter_pdf'),  # Add this line
]
