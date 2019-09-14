from django.urls import path
from . import views
from .views import CreatePostView, ListPostView, DetailPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', ListPostView.as_view(), name='index-blog'),
    path('create/', CreatePostView.as_view(), name='blog-post'),
    path('posts/<slug>/',  DetailPostView.as_view(), name='blog-view'),
    path('posts/<slug>/update/',  UpdatePostView.as_view(), name='blog-update'),
    path('posts/<slug>/delete/',  DeletePostView.as_view(), name='blog-delete'),
    path('about/', views.about, name='about-blog'),
]