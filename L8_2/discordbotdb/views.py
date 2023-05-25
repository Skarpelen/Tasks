from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, View, CreateView, UpdateView, DeleteView
from .forms import UserForm
from .models import User, Weapon, Grenade, Guild, Status


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


class WeaponsListView(ListView):
    model = Weapon
    template_name = 'discordbotdb/weapons_list.html'

    def get_queryset(self):
        self.user_id = self.kwargs['pk']
        weapon_list = Weapon.objects.filter(user_id=self.user_id)
        return weapon_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weapon_list'] = self.get_queryset()
        return context


class GrenadesListView(ListView):
    model = Grenade
    template_name = 'discordbotdb/grenades_list.html'

    def get_queryset(self):
        self.user_id = self.kwargs['pk']
        return Grenade.objects.filter(user_id=self.user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grenades_list'] = self.get_queryset()
        return context


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
