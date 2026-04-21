from django.core.management.base import BaseCommand, CommandError
from core.models import Student

class Command(BaseCommand):
    help = "Delete all students"

    def handle(self, *args, **options):
        try:
            count, _ = Student.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"Deleted {count} students"))
        except Exception as e:
            raise CommandError(f"Command failed: {str(e)}")