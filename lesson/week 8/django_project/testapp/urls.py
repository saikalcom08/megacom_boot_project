from django.urls import path
# from .views import index

from . import views

# urlpatterns = [
#     path("test/", views.index)
# ]

urlpatterns = [
    path("test/", views.index),
    path("django/", views.django_get_page)
]