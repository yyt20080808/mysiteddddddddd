from django.shortcuts import render,redirect
from django.http import HttpResponse
from firstproject.models import Column,Article
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    # print request.user

    # columns = Column.objects.all()
    return render(request,'index.html',{'home_display_columns': home_display_columns,
                                        'nav_display_columns': nav_display_columns,})
def baidumap_view(request):
    return render(request,'third-party/baidumap.html')

@login_required(login_url='/login/')
def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    print request.user
    return render(request,'news/column.html',{'column':column})

@login_required(login_url='/login/')
def article_detail(request,pk,article_slug):
    article = Article.objects.get(pk = pk)

    # re-direct
    if article.slug != article_slug:
        return redirect(article,permanent=True)

    return render(request,'news/article.html',{'article':article})
