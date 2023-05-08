from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('best_emp', views.best_emp),
    path('add_emp', views.add_emp)
]