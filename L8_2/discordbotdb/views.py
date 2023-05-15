from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import User, Weapon, Grenade, Guild, Status


def user_list(request):
    search_query = request.GET.get('search', '')
    users = User.objects.filter(name__icontains=search_query)
    context = {'users': users}
    return render(request, 'discordbotdb/users.html', context)


class HomeView(TemplateView):
    template_name = 'discordbotdb/home.html'


class UsersListView(ListView):
    model = User
    template_name = 'discordbotdb/users_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список пользователей'
        return context


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
