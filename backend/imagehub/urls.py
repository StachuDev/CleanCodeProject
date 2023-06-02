from django.urls import path , include
from imagehub import views


urlpatterns = [
    path('tags/', views.tag_list, name='tag-list'),
    path('tags/<int:pk>/', views.tag_detail, name='tag-detail'),
    path('posts/', views.post_list, name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/<int:pk>/edit/', views.edit_post, name='edit-post'),
    path('comments/', views.comment_list, name='comment-list'),
    path('comments/new/', views.add_comment, name='comment-new'),
    path('comments/<int:pk>/', views.comment_detail, name='comment-detail'),
    path('likes/', views.add_postlike, name='postlike-list'),
    path('likes/new/', views.add_postlike, name='postlike-new'),
    path('likes/<int:pk>/', views.postlike_detail, name='postlike-detail'),
    path('subcomments/', views.subcomment_list, name='subcomment-list'),
    path('subcomments/new/', views.add_subcomment, name='subcomments-new'),
    path('subcomments/<int:pk>/', views.subcomment_detail, name='subcomments-detail'),
]