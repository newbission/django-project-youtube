from django.core.management.base import BaseCommand
from django.db import connections
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Wating for DB connections ...")

        is_db_connected = None
        while not is_db_connected:
            try:
                is_db_connected = connections["default"]
            except:
                self.stdout.write("Retrying DB connections ...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("PostgreSQL DB Connection Success !!!"))
