from django import forms
from django.core.validators import RegexValidator

from .models import User


class UserForm(forms.ModelForm):
    user_discord_id = forms.CharField(validators=[RegexValidator(r'^[0-9]{17,20}$', 'Введите допустимый Discord ID ('
                                                                                    'от 17 до 20 цифр).')])

    class Meta:
        model = User
        fields = ['name', 'user_discord_id', 'guild']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['name'].label = 'Имя пользователя'
        self.fields['user_discord_id'].required = True
        self.fields['user_discord_id'].label = 'Discord ID пользователя'
        self.fields['guild'].required = True
        self.fields['guild'].label = 'Сервер'
