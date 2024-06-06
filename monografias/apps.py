from django.apps import AppConfig


class MonografiasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monografias'
class monografias(AppConfig):
 name = 'monografias'
 def ready(self):

    import monografias.signals