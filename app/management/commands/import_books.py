import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from app.models import Book

class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        filename = options['filename']
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            for row in reader:
                title, author, pub_date_str, description = row
                pub_date = datetime.strptime(pub_date_str, '%Y-%m-%d').date()
                Book.objects.create(title=title, author=author, published_date=pub_date, description=description)
