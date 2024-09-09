import json
from uuid import *

# from django.core import serializers
from django.http import HttpRequest, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from web.models import *


# Create your views here.
def index(request: HttpRequest):
    return render(
        request,
        "web/home.html",
        {
            "posts": Article.objects.filter(featured=True)[0:5],
        }
        )

def contact(request: HttpRequest):
    return render(
		request,
		"web/contact.html"
	)

def category_detail(request: HttpRequest, slug):
    category = get_object_or_404(Classification, slug=slug)
    articles = Article.objects.filter(article_classification=category).order_by('-date_published')
    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'posts': articles,
    }
    return render(request, 'web/category_articles.html', context)


def about(request: HttpRequest):
    return render(
		request,
		"web/about.html"
	)
    
def posts(request):
    article_list = Article.objects.all().order_by('-date_published')
    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'web/posts.html', {'posts': articles})
 
def article_view(request: HttpRequest, articleID: UUID):
    if request.method == "GET":
        return render(
            request,
            "web/article.html",
            {
                "page": Article.objects.get(article_id=articleID),
            }
        ) 


def search_result(request: HttpRequest, searchKey: str):
    if request.method == "POST":
        result = []
        t = Article.objects.all()
        for x in t:
            if searchKey in x.title:
                result.append(x)
            else:
                continue
        return JsonResponse({"articles": result}, status=200)


def author_page(request: HttpRequest, AuthorName: str):
    if request.method == "POST":
        t = Article.objects.filter(author=AuthorName)
        author_info = Author.objects.get(name=AuthorName)
        return JsonResponse(
            {"authorInformation": author_info, "articles": t}, status=200
        )


def comments(request: HttpRequest, articleID: str):
    article = Article.objects.get(article_id=articleID)
    if request.method == "GET":
        comments = ArticleComment.objects.filter(article=article)
        return JsonResponse({"Comments": comments}, status=200)
    if request.method == "POST":
        try:
            new_comment = ArticleComment(
                commenter=request.user,
                article=article,
                comment_content=json.loads(request.body)["comment_content"],
            )
            new_comment.save()
            return JsonResponse({"Message": "Comment Created Sucessfully"}, status=200)
        except Exception:
            return JsonResponse({"Message": "Error creating comment"}, status=400)


def like(request: HttpRequest, articleID: str):
    us = request.user
    article = Article.objects.get(article_id=articleID)
    if request.method == "POST":
        try:
            like = LikedArticle.objects.get(article=article, liker=us)
            like.delete()
        except LikedArticle.DoesNotExist:
            like = LikedArticle(article=article, liker=us)
            like.save()
        return JsonResponse(
            {"Message": "like request recieved and processed"}, status=200
        )
