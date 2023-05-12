from django.shortcuts import render
from django.views.generic import ListView
from .models import Users, Weapons, Grenades, Guild, Status


class UsersListView(ListView):
    model = Users
    template_name = 'discordbotdb/users_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список пользователей'
        return context


class WeaponsListView(ListView):
    model = Weapons
    template_name = 'discordbotdb/weapons_list.html'

    def get_queryset(self):
        self.user_id = self.kwargs['pk']
        weapon_list = Weapons.objects.filter(user_id=self.user_id)
        return weapon_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weapon_list'] = self.get_queryset()
        return context


class GrenadesListView(ListView):
    model = Grenades
    template_name = 'discordbotdb/grenades_list.html'

    def get_queryset(self):
        self.user_id = self.kwargs['pk']
        return Grenades.objects.filter(user_id=self.user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grenades_list'] = self.get_queryset()
        return context


class GuildsListView(ListView):
    model = Guild
    template_name = 'discordbotdb/guilds_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список гильдий'
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
