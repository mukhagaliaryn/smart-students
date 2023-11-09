from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('news-detail/<pk>/', views.news_detail, name='news_detail'),
    path('teachers/', views.teachers, name='teachers'),
    path('categories/', views.categories, name='categories'),
    path('category/<pk>/', views.category, name='category'),
    path('docs/', views.docs, name='docs'),
    path('docs/<pk>/', views.docs_detail, name='docs_detail'),
]