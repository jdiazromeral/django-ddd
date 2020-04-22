from django.apps import apps
from django.conf import settings
from django.contrib.admin import site
from django.test import SimpleTestCase

from django_ddd.apps_config import CleanAppConfig
from dummy_app.infrastructure.models import CustomModel


class TestCleanAppConfig(SimpleTestCase):
    def setUp(self) -> None:
        self.app_admin = apps.get_app_config("dummy_app")

    def test_app_config_custom_modules(self):
        class CustomAppConfig(CleanAppConfig):
            path = "custom_path"

        app_config = CustomAppConfig("label", "module")

        self.assertEqual("infrastructure.models", app_config.CUSTOM_MODELS_MODULE)
        self.assertEqual("infrastructure.migrations", app_config.CUSTOM_MIGRATIONS_MODULE)
        self.assertEqual("infrastructure.admin", app_config.CUSTOM_ADMIN_MODULE)

    def test_custom_modules_module(self):
        self.assertEqual("infrastructure.models", self.app_admin.CUSTOM_MODELS_MODULE)
        self.assertEqual("dummy_app.infrastructure.models", self.app_admin.models_module.__name__)

    def test_custom_migrations_module(self):
        self.assertEqual("infrastructure.migrations", self.app_admin.CUSTOM_MIGRATIONS_MODULE)
        self.assertEqual("dummy_app.infrastructure.migrations", settings.MIGRATION_MODULES["dummy_app"])

    def test_custom_admin_registers_models(self):
        self.assertEqual("infrastructure.admin", self.app_admin.CUSTOM_ADMIN_MODULE)
        self.assertTrue(site.is_registered(CustomModel))
