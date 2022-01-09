from  django.urls import path
from .views import *

urlpatterns = [
    path('h/',hey),
    path('a/',a),
    path('register/',register,name='register'),
    path('login/',signin,name='login'),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('info/',info,name='info'),
    path('contact/',contact,name='contact'),
    path('index/',index,name='index'),
    path('book/',book,name='book'),
    path('booknew/',booknew,name='booknew'),
    path('bookview/<int:pk>',bookview,name='bookview'),
    path('proview/<int:ok>',proview,name='proview')
]