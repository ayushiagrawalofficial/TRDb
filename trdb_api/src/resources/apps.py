from django.apps import AppConfig


class ResourcesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "resources"

    def ready(self):
        from resources.signals import resources_signal
        from resources.receivers import (
            increment_vote_count_receiver,
            decrement_vote_count_receiver,
        )

        resources_signal.connect(
            increment_vote_count_receiver, decrement_vote_count_receiver
        )
