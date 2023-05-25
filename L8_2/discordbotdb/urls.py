from django.urls import path
from .views import (
    UsersListView,
    GuildsListView,
    WeaponsListView,
    GrenadesListView,
    StatusListView,
    HomeView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', UsersListView.as_view(), name='users'),
    path('guilds/', GuildsListView.as_view(), name='guilds'),
    path('weapons/<int:pk>/', WeaponsListView.as_view(), name='weapons'),
    path('grenades/<int:pk>/', GrenadesListView.as_view(), name='grenades'),
    path('status/<int:pk>/', StatusListView.as_view(), name='status'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
