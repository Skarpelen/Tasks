from django.urls import include, path
from rest_framework import routers
from .views import (
    UsersListView,
    GuildsListView,
    StatusListView,
    HomeView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    GuildViewSet, UserViewSet, StatusViewSet, WeaponViewSet, GrenadeViewSet
)

router = routers.DefaultRouter()
router.register('guilds', GuildViewSet)
router.register('users', UserViewSet)
router.register('statuses', StatusViewSet)
router.register('weapons', WeaponViewSet)
router.register('grenades', GrenadeViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/', include(router.urls)),
    path('users/', UsersListView.as_view(), name='users'),
    path('guilds/', GuildsListView.as_view(), name='guilds'),
    path('status/<int:pk>/', StatusListView.as_view(), name='status'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
