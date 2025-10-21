from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts_index, name="index"),
    path("posts", views.posts, name="posts"),
    path("sections/<int:num>", views.section, name="section"),
    path('hello/', views.hello_world, name='hello_world'),
    path('singlepage/', views.single_page_app, name='single_page_app'),
    path('scroll/', views.scroll_page, name='scroll_page'),
    path('webpage/', views.webpage, name='webpage'),
    path('animate/', views.animate, name='animate'),
    path('move/', views.move, name='move'),
    path('react-app/', views.react_app, name='react_app'),
]