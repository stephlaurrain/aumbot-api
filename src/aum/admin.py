from django.contrib import admin
from aum.models import Visit


class VisitAdmin(admin.ModelAdmin):

    list_display = ('aum_id', 'username')

admin.site.register(Visit, VisitAdmin)
