from django.urls import path
from . import views

app_name = 'posts'
app_name = 'group_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('author/', views.AboutAuthorView.as_view()),
    path('tech/', views.AboutTechView.as_view()),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path("create/", views.post_create, name="create"),
    path('posts/<int:post_id>/edit/',
         views.post_edit, name='post_edit'),
]
