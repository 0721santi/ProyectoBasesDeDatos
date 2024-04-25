from django.urls import path
from . import views

urlpatterns = [
    path('', views.init),
    path('index.html', views.init),
    path('CRUD/create.html', views.create),
    path('CRUD/delete.html', views.delete),
    path('CRUD/retrieve.html', views.retrieve),
    path('CRUD/update.html', views.update),
]