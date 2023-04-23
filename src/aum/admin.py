from django.contrib import admin
from aum.models.visit import Visit
from aum.models.ban import Ban
from aum.models.charm import Charm

class VisitAdmin(admin.ModelAdmin):

    list_display = ('id', 'aum_id', 'username')

admin.site.register(Visit, VisitAdmin)


class BanAdmin(admin.ModelAdmin):

    list_display = ('id', 'aum_id', 'done')

admin.site.register(Ban, BanAdmin)


class CharmAdmin(admin.ModelAdmin):

    list_display = ('id', 'aum_id', 'date_charm')

admin.site.register(Charm, CharmAdmin)
