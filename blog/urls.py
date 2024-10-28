# blog/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'blog'
urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # List all blog posts
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),  # View a single blog post
    path('new/', views.blog_create, name='blog_create'),  # Create a new blog post
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('register/', views.register, name='register'),  # Registration URL
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='blog/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/<int:user_id>/', views.user_profile_view, name='user_profile'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'), 
    path('profile/edit/', views.edit_profile, name='edit_profile'),
   

    # Admin URLs
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/users/', views.user_management, name='user_management'),
    path('admin/posts/', views.post_management, name='post_management'),
    path('admin/users/block/<int:user_id>/', views.block_user, name='block_user'), 
    path('admin/delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('admin/unblock_user/<int:user_id>/', views.unblock_user, name='unblock_user'),
     path('admin/users/block/<int:user_id>/', views.block_user, name='block_user'),  # Block a user
    path('admin/delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('admin/unblock_user/<int:user_id>/', views.unblock_user, name='unblock_user'),  # Unblock a user
    path('admin/user/<int:user_id>/', views.user_detail, name='user_detail'), 
     path('admin/users/delete/<int:user_id>/', views.delete_user, name='delete_user'), 
]
