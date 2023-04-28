from django.contrib import admin
from aum.models.visit import Visit
from aum.models.ban import Ban
from aum.models.charm import Charm
from aum.models.contact import Contact
from aum.models.favorite import Favorite
from aum.models.distance import Distance
from aum.models.keyword import Keyword
from aum.models.stat import Stat

class VisitAdmin(admin.ModelAdmin):

    list_display = ('id', 'aum_id', 'username',
        'city', 'distance', 'age', 'title', 'measurement', 'nb_photo',
        'description', 'shopping', 'crack', 'cant_stand', 'popularity', 'hot', 'score',
        'date_visit', 'date_first_visit', 'full_desc', 'full_shopping')

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


class DistanceAdmin(admin.ModelAdmin):

    list_display = ('id', 'city', "km")

admin.site.register(Distance, DistanceAdmin)


class KeywordAdmin(admin.ModelAdmin):

    list_display = ('id', 'word', "weight")

admin.site.register(Keyword, KeywordAdmin)

class StatAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_stat', 'age_min', 'age_min', 'nb_online')

admin.site.register(Stat, StatAdmin)