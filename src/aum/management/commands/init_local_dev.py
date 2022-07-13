from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

UserModel = get_user_model()

ADMIN_ID = 'bigadm'
ADMIN_PASSWORD = 'noway'
USER_ID = 'steph'
USER_PASSWORD = 'noway'


class Command(BaseCommand):

    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))
        UserModel.objects.create_superuser(ADMIN_ID, 'admin@commerce-numerique.com', ADMIN_PASSWORD)
        UserModel.objects.create_user(USER_ID, 'steph@commerce-numerique.com', USER_PASSWORD, is_staff=True)

        self.stdout.write(self.style.SUCCESS("All Done !"))
