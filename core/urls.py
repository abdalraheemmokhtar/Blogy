from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:author_id>/', views.post_details, name='post_details'),
    path('create/', views.create_post, name='create_post'),
]
