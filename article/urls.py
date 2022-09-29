from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('detail<int:id>', views.article_detail, name='article_detail'),
]
