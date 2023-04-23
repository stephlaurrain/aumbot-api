from django.contrib import admin
from aum.models.visit import Visit
from aum.models.ban import Ban
from aum.models.charm import Charm
from aum.models.contact import Contact
from aum.models.favorite import Favorite
from aum.models.distance import Distance
from aum.models.keyword import Keyword


class VisitAdmin(admin.ModelAdmin):

    list_display = ('id', 'aum_id', 'username')

admin.site.register(Visit, VisitAdmin)


class BanAdmin(admin.ModelAdmin):

    list_display = ('id', 'aum_id', 'done')

admin.site.register(Ban, BanAdmin)


class CharmAdmin(admin.ModelAdmin):

    list_display = ('id', 'aum_id', 'date_charm')

admin.site.register(Charm, CharmAdmin)


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'aum_id')

admin.site.register(Contact, ContactAdmin)


class FavoriteAdmin(admin.ModelAdmin):

    list_display = ('id', 'aum_id')

admin.site.register(Favorite, FavoriteAdmin)