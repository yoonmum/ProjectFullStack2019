from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Binding, Publisher, Transaction,Book ,Borrow
from .forms import BookForm
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

    
def show(request):
    context = dict()
    return render(request, 'example_app/index2.html', context)


@login_required
def logoutView(request):
    logout(request)
    return redirect('home')

def list_book(request):
    context = dict()
    context['books'] = Book.objects.all().order_by('book')
    return render(request, 'example_app/listbook.html', context)

def add_book(request):
    context = dict()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = BookForm()
    context['form'] = form
    return render(request, 'example_app/addbook.html', context)

def borrow_book(request,pk):
    context = dict()
    if request.method =='POST' :
        try:
            actor = User.objects.fisrt_name
            book = Book.objects.get(pk=pk)
            status = bool(request.POST['status'])
            if status == True : 
                book.status = "False"
                book.save()
                Transaction.objects.create(
                    actor = actor,
                    book =book,
                # status = status,
                # total_price = item.price * amount,
                )
                return redirect('listbook')
            else:
                 return redirect('listbook')
        except Exception as e:
            print(e)
            return redirect('listbook')
    else:
        book = Book.objects.get(pk=pk)
        context = {'book' : book}
        return render(request, 'borrowbook.html', context)
