import os
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from aum.management.commands.exported.ban import BAN
from aum.management.commands.exported.keyword import KEYWORD
from aum.management.commands.exported.contact import CONTACT
from aum.management.commands.exported.distance import DISTANCE
from aum.models.visit import Visit
from aum.models.ban import Ban
from aum.models.charm import Charm
from aum.models.contact import Contact
from aum.models.favorite import Favorite
from aum.models.distance import Distance
from aum.models.keyword import Keyword

UserModel = get_user_model()

load_dotenv()
ADMIN_ID = os.getenv('ADMIN_ID')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
ADMIN_MAILBOX = os.getenv('ADMIN_MAILBOX')
USER_ID = os.getenv('USER_ID')
USER_PASSWORD = os.getenv('USER_PASSWORD')
USER_MAILBOX = os.getenv('USER_MAILBOX')





class Command(BaseCommand):

    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))
        
        # init data
        Ban.objects.all().delete()
        for line in BAN:
            Ban.objects.create(aum_id=line['aum_id'], done=line['done'])

        Contact.objects.all().delete()
        for line in CONTACT:
            Contact.objects.create(aum_id=line['aum_id'])

        Distance.objects.all().delete()
        for line in DISTANCE:
            Distance.objects.create(city=line['city'], km=line['km'])

        Keyword.objects.all().delete()
        for line in KEYWORD:
            Keyword.objects.create(word=line['word'], weight=line['weight'])

        #init users
        UserModel.objects.all().delete();
        UserModel.objects.create_superuser(ADMIN_ID, ADMIN_MAILBOX, ADMIN_PASSWORD)
        UserModel.objects.create_user(USER_ID, USER_MAILBOX, USER_PASSWORD, is_staff=True)

        self.stdout.write(self.style.SUCCESS("All Done !"))
