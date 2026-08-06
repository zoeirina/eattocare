from django.apps import AppConfig
import os

class NutritionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nutrition'

    def ready(self):
        # Solo intentamos crear el superusuario si estamos en producción y existen las variables
        if os.environ.get('RENDER'):
            from django.contrib.auth import get_user_model
            User = get_user_model()
            username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'irina.torrealba@gmail.com')
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'rintus-quvnuV-jyqzu7')
            
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)