from django.urls import path
from .views import UsersListView, GuildsListView, WeaponsListView, GrenadesListView, StatusListView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', UsersListView.as_view(), name='users'),
    path('guilds/', GuildsListView.as_view(), name='guilds'),
    path('weapons/<int:pk>/', WeaponsListView.as_view(), name='weapons'),
    path('grenades/<int:pk>/', GrenadesListView.as_view(), name='grenades'),
    path('status/<int:pk>/', StatusListView.as_view(), name='status'),
]