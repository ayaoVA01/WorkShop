from django.shortcuts import render
from category.models import Category
from .models import Blogs
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.
def index(request):
    categories= Category.objects.all()
    blog =Blogs.objects.all()
    latest = Blogs.objects.all().order_by('-pk')[:2]

    # pagination
    paginator = Paginator(blog,3)
    try:
       page = request.GET.get('page','1')#page is tua pes
    except:
        page = 1
    try:
        blogPerpage =paginator.page(page)
    except(EmptyPage,InvalidPage):
        blogPerpage=Paginator.page(paginator.num_pages)


    return render(request, 'frontend/index.html',{
        'categories':categories,
        'blogs':blogPerpage,
        'latest':latest
    })