# Generated by Django 4.2.1 on 2023-05-12 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('server_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('server_name', models.TextField()),
                ('prefix', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('user_discord_id', models.BigIntegerField()),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discordbotdb.guild')),
            ],
        ),
        migrations.CreateModel(
            name='Weapons',
            fields=[
                ('weapon_id', models.AutoField(primary_key=True, serialize=False)),
                ('weapon_name', models.TextField()),
                ('current_ammo', models.IntegerField()),
                ('inventory_name', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discordbotdb.users')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('armour', models.CharField(max_length=255)),
                ('head', models.IntegerField()),
                ('body', models.IntegerField()),
                ('l_hand', models.IntegerField()),
                ('r_hand', models.IntegerField()),
                ('l_foot', models.IntegerField()),
                ('r_foot', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='discordbotdb.users')),
            ],
        ),
        migrations.CreateModel(
            name='Grenades',
            fields=[
                ('grenade_id', models.AutoField(primary_key=True, serialize=False)),
                ('grenade_name', models.TextField()),
                ('amount', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discordbotdb.users')),
            ],
        ),
    ]
