from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('teachers/', views.teachers, name='teachers'),
    path('categories/', views.categories, name='categories'),
    path('docs/', views.docs, name='docs'),
]