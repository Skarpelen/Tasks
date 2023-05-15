from django.db import models


class Guild(models.Model):
    guild_id = models.AutoField(primary_key=True)
    server_id = models.BigIntegerField()
    server_name = models.TextField()
    prefix = models.TextField(default='+')

    def __str__(self):
        return self.server_name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    user_discord_id = models.BigIntegerField()
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    armour = models.CharField(max_length=255)
    head = models.IntegerField()
    body = models.IntegerField()
    l_hand = models.IntegerField()
    r_hand = models.IntegerField()
    l_foot = models.IntegerField()
    r_foot = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Status for user {self.user.name}"


class Weapon(models.Model):
    weapon_id = models.AutoField(primary_key=True)
    weapon_name = models.TextField()
    current_ammo = models.IntegerField()
    inventory_name = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.weapon_name


class Grenade(models.Model):
    grenade_id = models.AutoField(primary_key=True)
    grenade_name = models.TextField()
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.grenade_name

