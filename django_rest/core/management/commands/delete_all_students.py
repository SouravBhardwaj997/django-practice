from django.core.management.base import BaseCommand, CommandError
from core.models import Student
class Command(BaseCommand):
    help="Delete All studentss"
    def handle(self, *args, **options):
        try:
            students=Student.objects.all()
            print("students",students)
        except:
            raise CommandError("Command not working")