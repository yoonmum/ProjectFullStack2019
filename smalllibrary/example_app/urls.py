from django.urls import path
from .views import auth_page, home, logoutView , show, borrow_book

app_name = 'example_app'

urlpatterns = [
    path('', home, name='home'),
    path('show/', show, name='show'),
    path('auth_page/', auth_page, name='auth_page'),
    path('borrow/<int:pk>/', borrow_book , name='borrow_book'),
    path('logout/', logoutView, name='logout'),   
]
