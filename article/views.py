from django.shortcuts import render, redirect, get_object_or_404
from article.models import Article
import re


def article_detail(request, id):
    # 获取文章
    article = get_object_or_404(Article, id=id)
    context = {'article': article}
    return render(request, 'article/article_detail.html', context)


def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'article/article_list.html', context)
