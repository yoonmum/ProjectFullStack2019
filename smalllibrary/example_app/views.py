from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Binding, Publisher, Transaction,Book ,Borrow
# Create your views here.

@login_required
def auth_page(request):
    return render(request, 'example_app/auth_page.html')

def home(request):
    context = dict()

    if request.user.is_authenticated:
        context['greeting'] = 'Welcome Back {}'.format(request.user)
    else:
        context['greeting'] = 'Welcome Anonymous'

    return render(request, 'example_app/home.html', context)

@login_required
def logoutView(request):
    logout(request)
    return redirect('home')

def list_book(request):
    context = dict()
    context['books'] = Book.objects.all().order_by('book')
    return render(request, 'listbook.html', context)

def add_book(request):
    context = dict()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = ItemForm()
    context['form'] = form
    return render(request, 'addbook.html', context)
