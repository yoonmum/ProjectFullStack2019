from django.urls import path
from .views import auth_page, home, logoutView , show

app_name = 'example_app'

urlpatterns = [
    path('', home, name='home'),
    path('show/', show, name='show'),
    path('auth_page/', auth_page, name='auth_page'),
    path('logout/', logoutView, name='logout'),   
]
