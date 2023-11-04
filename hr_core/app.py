from django.apps import AppConfig

class hr_coreAppConfig(AppConfig):
    name = "hr_core"

    def ready(self):
        from hr_core import signals # pylint: disable=unused-variable
