from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Weapon, Grenade, Guild, Status
from .forms import UserForm


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(name='John Doe')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discordbotdb/home.html')

    def test_user_create_view(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discordbotdb/user_create.html')

        form_data = {'name': 'Alice'}
        response = self.client.post(reverse('user_create'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)

    def test_user_update_view(self):
        url = reverse('user_update', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discordbotdb/user_update.html')

        form_data = {'name': 'Jane'}
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, 'Jane')

    def test_user_delete_view(self):
        url = reverse('user_delete', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discordbotdb/user_delete.html')

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())

    def test_users_list_view(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discordbotdb/users_list.html')

    def test_weapons_list_view(self):
        url = reverse('weapons', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discordbotdb/weapons_list.html')

    def test_grenades_list_view(self):
        url = reverse('grenades', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discordbotdb/grenades_list.html')

    def test_guilds_list_view(self):
        response = self.client.get(reverse('guilds'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discordbotdb/guilds_list.html')

    def test_status_list_view(self):
        url = reverse('status', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discordbotdb/status_list.html')


class FormTestCase(TestCase):
    def test_user_form(self):
        form_data = {'name': 'John Doe'}
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {'name': ''}
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])
