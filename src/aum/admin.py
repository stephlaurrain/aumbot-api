from django.contrib import admin
from aum.models.visit import Visit
from aum.models.ban import Ban

class VisitAdmin(admin.ModelAdmin):

    list_display = ('aum_id', 'username')

admin.site.register(Visit, VisitAdmin)

class BanAdmin(admin.ModelAdmin):

    list_display = ('aum_id', 'done')

admin.site.register(Ban, BanAdmin)
