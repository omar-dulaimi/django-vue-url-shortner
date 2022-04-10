from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from urlshortner.models import UserUrl


class Command(BaseCommand):
    help = 'Deletes the old urls past 10days'

    def handle(self, *args, **options):
        try:
            past = timezone.datetime.today() - timezone.timedelta(days=10)
            UserUrl.objects.filter(created__lte=past).delete()
        except:
            raise CommandError('Failed to remove old urls')
        # success message
        self.stdout.write('Successfully removed all old urls')
