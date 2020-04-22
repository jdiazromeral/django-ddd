from importlib import import_module

from django.apps import AppConfig
from django.conf import settings
from django.contrib.admin import site, AdminSite
from django.utils.module_loading import autodiscover_modules


class CleanAppConfig(AppConfig):
    CUSTOM_MODELS_MODULE = getattr(settings, "CUSTOM_MODELS_MODULE", "models")
    CUSTOM_MIGRATIONS_MODULE = getattr(settings, "CUSTOM_MIGRATIONS_MODULE", "migrations")
    CUSTOM_ADMIN_MODULE = getattr(settings, "CUSTOM_ADMIN_MODULE", "admin")

    def import_models(self) -> None:
        super().import_models()
        self.__load_custom_models_module()

    def __load_custom_models_module(self) -> None:
        self.models_module = import_module(f"{self.label}.{self.CUSTOM_MODELS_MODULE}")

    def ready(self) -> None:
        self.__load_custom_admin_module(self.CUSTOM_ADMIN_MODULE, register_to=site)
        self.__load_custom_migration_module(self.CUSTOM_MIGRATIONS_MODULE)

    def __load_custom_admin_module(self, admin_module: str, register_to: AdminSite) -> None:
        autodiscover_modules(admin_module, register_to=register_to)

    def __load_custom_migration_module(self, migration_module: str) -> None:
        settings.MIGRATION_MODULES.update(**{self.label: f"{self.label}.{migration_module}"})
