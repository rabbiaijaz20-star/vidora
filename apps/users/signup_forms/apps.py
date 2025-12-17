from django.apps import AppConfig

class SignupFormsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users.signup_forms'   # ✅ must match INSTALLED_APPS