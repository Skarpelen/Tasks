from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, View, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .forms import UserForm
from .models import User, Guild, Status, Weapon, Grenade
from .serializers import GuildSerializer, UserSerializer, StatusSerializer, WeaponSerializer, GrenadeSerializer


class HomeView(TemplateView):
    template_name = 'discordbotdb/home.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'discordbotdb/user_create.html'
    success_url = reverse_lazy('users')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'discordbotdb/user_update.html'
    success_url = reverse_lazy('users')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'discordbotdb/user_delete.html'
    success_url = reverse_lazy('users')


class UsersListView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        users = User.objects.filter(name__icontains=search_query)
        context = {'users': users, 'search_query': search_query}
        return render(request, 'discordbotdb/users_list.html', context)


class GuildsListView(ListView):
    model = Guild
    template_name = 'discordbotdb/guilds_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список серверов'
        return context


class StatusListView(ListView):
    model = Status
    template_name = 'discordbotdb/status_list.html'
    context_object_name = 'status'

    def get_queryset(self):
        self.user_id = self.kwargs['pk']
        return Status.objects.filter(user_id=self.user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статус'
        context['user_id'] = self.user_id
        return context


class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class GrenadeViewSet(viewsets.ModelViewSet):
    queryset = Grenade.objects.all()
    serializer_class = GrenadeSerializer
