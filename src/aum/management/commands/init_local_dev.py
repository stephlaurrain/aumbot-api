import os
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from aum.models import Keyword

UserModel = get_user_model()

load_dotenv()
ADMIN_ID = os.getenv('ADMIN_ID')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
ADMIN_MAILBOX = os.getenv('ADMIN_MAILBOX')
USER_ID = os.getenv('USER_ID')
USER_PASSWORD = os.getenv('USER_PASSWORD')
USER_MAILBOX = os.getenv('USER_MAILBOX')

KEYWORDS = [
    { 'word': 'genereuse', 'weight': 5},
        { 'word': 'pulpeuse', 'weight': 5},
        { 'word': 'fairelesmagasin', 'weight': 1},
        { 'word': 'fairedushopping', 'weight': 1},
        { 'word': 'jesuismoi', 'weight': 3},
        { 'word': 'jesuisentiere', 'weight': 3},
        { 'word': 'manquederespect', 'weight': 2},
        { 'word': 'partager', 'weight': 3},
        { 'word': 'profiter', 'weight': 3},
        { 'word': 'simple', 'weight': 1},
        { 'word': 'insta', 'weight': 4},
        { 'word': 'instagram', 'weight': 4},
        { 'word': 'vegan', 'weight': 4},
        { 'word': 'pasfaciledesepresenter', 'weight': 1},
        { 'word': 'moimeme', 'weight': 1},
        { 'word': 'honnete', 'weight': 2},
        { 'word': 'maman', 'weight': 2},
        { 'word': 'mensonge', 'weight': 2},
        { 'word': 'mauvaisefoi', 'weight': 2},
        { 'word': 'simplicite', 'weight': 3},
        { 'word': 'ouverte', 'weight': 1},
        { 'word': 'gensouverts', 'weight': 1},
        { 'word': 'faitesmoirire', 'weight': 4},
        { 'word': 'soyezoriginaux', 'weight': 4},
        { 'word': 'celibataire', 'weight': 4},
        { 'word': 'adecouvrir', 'weight': 2},
        { 'word': 'medecouvrir', 'weight': 2},
        { 'word': 'feeling', 'weight': 5},
        { 'word': 'brindefolie', 'weight': 5},
        { 'word': 'menteur', 'weight': 3},
        { 'word': 'ouverturedespri', 'weight': 1},
        { 'word': 'altruisme', 'weight': 1},
        { 'word': 'jenesaispascequejefaisla', 'weight': 1},
        { 'word': 'desedecrire', 'weight': 3},
        { 'word': 'salsa', 'weight': 1},
        { 'word': 'voyage', 'weight': 1},
        { 'word': 'attentionne', 'weight': 1},
        { 'word': 'graindefolie', 'weight': 3},
        { 'word': 'respectueux', 'weight': 1},
        { 'word': 'gentil', 'weight': 3},
        { 'word': 'motard', 'weight': 1},
        { 'word': 'ronde', 'weight': 4},
        { 'word': 'franche', 'weight': 2},
        { 'word': 'sociable', 'weight': 1},
        { 'word': 'fidele', 'weight': 1},
        { 'word': 'cheval', 'weight': 1},
        { 'word': 'prisedetete', 'weight': 2},
        { 'word': 'hyprocrisie', 'weight': 1},
        { 'word': 'authentique', 'weight': 1},
        { 'word': 'infidelite', 'weight': 2},
        { 'word': 'enrichir', 'weight': 3},
        { 'word': 'snap', 'weight': 5},
        { 'word': 'nemordspas', 'weight': 2},
        { 'word': 'ambitieu', 'weight': 2},
        { 'word': 'faineant', 'weight': 2},
        { 'word': 'avosclavier', 'weight': 4},
        { 'word': 'bellesurprise', 'weight': 4},
        { 'word': 'biendansses', 'weight': 4},
        { 'word': 'biendansa', 'weight': 4},
        { 'word': 'saiscequilveut', 'weight': 3},
        { 'word': 'entiere', 'weight': 2},
        { 'word': 'bellerencontre', 'weight': 2},
        { 'word': 'passerieux', 'weight': 3},
        { 'word': 'seconddegre', 'weight': 3},
        { 'word': 'equilibre', 'weight': 1},
        { 'word': 'confiance', 'weight': 2},
        { 'word': 'complicite', 'weight': 2},
        { 'word': 'gentleman', 'weight': 1},
        { 'word': 'misogyne', 'weight': 4},
        { 'word': 'beauf', 'weight': 4},
        { 'word': 'arrogant', 'weight': 3},
        { 'word': 'radin', 'weight': 5},
        { 'word': 'apprendreaseconnaitre', 'weight': 4},
        { 'word': 'ig:', 'weight': 5},
        { 'word': 'naturel', 'weight': 1},
        { 'word': 'romantique', 'weight': 3},
        { 'word': 'grandcoeur', 'weight': 3},
        { 'word': 'riche', 'weight': 2},
        { 'word': 'attachiante', 'weight': 1},
        { 'word': 'macho', 'weight': 2},
        { 'word': 'tropsurdeu', 'weight': 2},
        { 'word': 'transparence', 'weight': 2},
        { 'word': 'perver', 'weight': 3},
        { 'word': 'famille', 'weight': 3},
        { 'word': 'coupdecoeur', 'weight': 2},
        { 'word': 'caseenmoin', 'weight': 3},
        { 'word': 'casesenmoin', 'weight': 3},
        { 'word': '30kg', 'weight': 5},
        { 'word': 'serieu', 'weight': 3},
        { 'word': 'souffert', 'weight': 3},
        { 'word': 'plancul', 'weight': 1},
        { 'word': 'prisesdetete', 'weight': 3},
        { 'word': 'planq', 'weight': 1},
        { 'word': 'soindemoi', 'weight': 3},
        { 'word': 'fofolle', 'weight': 4},
        { 'word': 'paslatete', 'weight': 3},
        { 'word': 'chien', 'weight': 1},
        { 'word': 'franchise', 'weight': 2},
        { 'word': 'fleurdepeau', 'weight': 2},
        { 'word': 'piedssurterre', 'weight': 2},
        { 'word': 'planscul', 'weight': 1},
        { 'word': 'relationdifficile', 'weight': 4},
        { 'word': 'chieuse', 'weight': 3},
        { 'word': '175cm', 'weight': 10},
        { 'word': '180cm', 'weight': 10},
        { 'word': '80kg', 'weight': 10},
        { 'word': '95kg', 'weight': 10},
        { 'word': '70kg', 'weight': 10}
]



class Command(BaseCommand):

    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))
        
        # init keywords
        Keyword.objects.all().delete()

        for data_keyword in KEYWORDS:
            Keyword.objects.create(word=data_keyword['word'], weight=data_keyword['weight'])

        #init users
        UserModel.objects.all().delete();
        UserModel.objects.create_superuser(ADMIN_ID, ADMIN_MAILBOX, ADMIN_PASSWORD)
        UserModel.objects.create_user(USER_ID, USER_MAILBOX, USER_PASSWORD, is_staff=True)

        self.stdout.write(self.style.SUCCESS("All Done !"))
