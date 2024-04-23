
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name="Home"),
    path('signIn', signIn,name="signIn"),
    path('signOut', signOut,name="signOut"),
    
    path('add_product', add_product,name="add_product"),
    path('update/<int:id>', update,name="update"),
    path('delete/<int:id>', delete,name="add_product"),
    path('get_details', get_details,name="get_details"),
    
]
