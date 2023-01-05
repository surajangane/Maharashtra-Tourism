from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home),
    path('book',v.book),
    path('packages',v.packages),
    path('contact',v.Contact),
    path('gallery',v.gallery),
    path('my_booking',v.my_booking),
    path('login',v.user_login),
    path('logout',v.user_logout),
    path('register',v.register),
     path('set',v.setsession),
    path('get',v.getsession),
    path('editform/<int:rid>',v.editform),
    path('delete/<int:rid>',v.delete),
]
