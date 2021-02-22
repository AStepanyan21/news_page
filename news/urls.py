from django.urls import path

from . import views

urlpatterns = [
    path('', views.news_page, name='index'),
    path('categories/<str:categories_name>/', views.categories_page),
    path('<int:news_id>/', views.detail_page)
]
