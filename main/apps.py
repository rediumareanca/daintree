from django.apps import AppConfig
from elasticsearch_dsl.connections import connections


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        connections.create_connection()
