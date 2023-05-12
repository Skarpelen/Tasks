from django.contrib import admin
from .models import Guild, Users, Status, Weapons, Grenades

admin.site.register(Guild)
admin.site.register(Users)
admin.site.register(Status)
admin.site.register(Weapons)
admin.site.register(Grenades)