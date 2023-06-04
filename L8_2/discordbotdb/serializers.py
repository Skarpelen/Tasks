from rest_framework import serializers
from .models import Guild, User, Status, Weapon, Grenade


class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class GrenadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grenade
        fields = '__all__'
