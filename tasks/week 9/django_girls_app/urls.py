from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="all_posts"),
    # path('detail/<int:pk>/', views.detail_post, name='detail'),
    # path('delete/<int:pk>/', views.delete_post, name='delete')
]