from django.urls import path
from .import views

urlpatterns = [
    path('blog_list/', views.blog_list, name="blog_list"),
    path('register/', views.register_user, name='register_user'),
]