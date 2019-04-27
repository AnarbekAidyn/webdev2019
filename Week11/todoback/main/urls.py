from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path('main/task_lists',views.task_lists),
    path('main/task_lists/<int:pk>',views.task_ls_detail),
    path('main/task_lists/<int:pk>/tasks',views.task)
]
