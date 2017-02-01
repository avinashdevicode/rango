from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from models import Category, Page
from rango.forms import CategoryForm, PageForm
from datetime import datetime

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'pages': pages_list}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'username':'Avinash'}
    return render(request, 'rango/about.html', context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category).order_by('-views')[:5]
        context_dict['pages'] = pages
        context_dict['category'] = category
        
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
        
    return render(request, 'rango/category.html', context_dict)

def add_category(request):
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("/")
        else:
            print(form.errors)
            
    return render(request, 'rango/add_category.html', {'form':form})

def add_page(request, category_name_slug):
    form = PageForm()
    if request.method == "POST":
        form = PageForm(request.POST)
        try:
            cat = Category.objects.get(slug=category_name_slug)
        except Category.DoesNotExist:
            cat = None
            
        if cat and form.is_valid():
            page = form.save(commit = False)
            page.category = cat
            page.views = 0
            page.first_visit = datetime.now()
            page.last_visit = datetime.now()
            page.save()
            return show_category(request, category_name_slug)
        else:
            print form.errors
    context_dict = {'form':form, 'slug':category_name_slug}
    return render(request, 'rango/add_page.html', context_dict)


    