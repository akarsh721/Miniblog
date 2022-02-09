from collections import namedtuple
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('dashboard/',views.dashbaord,name="dashboard"),
    path('userlogin/',views.userlogin,name="login"),
    path('signup/',views.signup,name="signup"),
    path('userlogout/',views.userlogout,name="logout"),
    path('dashboard/newpost/',views.createPost,name="newpost"),
    path('dashboard/updatepost/<int:id>',views.updatepost,name="updatepost"),
    path('dashboard/deletepost/<int:id>',views.deletepost,name="deletepost"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminpanel/showpost/<username>',views.showpost,name="showpost"),
    path('adminpanel/',views.adminpanel,name="adminpanel"),
    path('adminpanel/removeauthor/<int:id>',views.adminRemoveAuthor,name="removeauthor"),
]