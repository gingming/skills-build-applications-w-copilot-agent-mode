from django.apps import AppConfig


class OctofitTrackerAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "octofit_tracker_app"

    def ready(self):
        print("octofit_tracker_app is being loaded")
