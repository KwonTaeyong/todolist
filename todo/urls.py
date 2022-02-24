from django.contrib import admin
from django.urls import path
from .views import IndexView, DetailView, DeleteView, UpdateView, TodoCreate

app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name='todolist'),
    path('detail/<int:pk>/', DetailView.as_view(), name="todolist_detail"),
    path('delete/<int:pk>/', DeleteView.as_view(), name="todolist_delete"),
    path('update/<int:pk>', UpdateView.as_view(), name="todolist_update"),
    path('create/', TodoCreate, name='todolist_create'),
]
