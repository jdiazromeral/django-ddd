import os
import shutil

from django.core.management import call_command
from django.test import SimpleTestCase


class TestCommand(SimpleTestCase):
    def test_command_creates_files(self):
        call_command("start_clean_app", "dummy_generated_app")
        self.assertTrue(os.path.exists(f"{os.getcwd()}/dummy_generated_app"))
        self.assertTrue(os.path.exists(f"{os.getcwd()}/dummy_generated_app/application"))
        self.assertTrue(os.path.exists(f"{os.getcwd()}/dummy_generated_app/domain"))
        self.assertTrue(os.path.exists(f"{os.getcwd()}/dummy_generated_app/infrastructure"))
        self.assertTrue(os.path.exists(f"{os.getcwd()}/dummy_generated_app/infrastructure/migrations"))
        self.assertTrue(os.path.exists(f"{os.getcwd()}/dummy_generated_app/infrastructure/models.py"))
        self.assertTrue(os.path.exists(f"{os.getcwd()}/dummy_generated_app/infrastructure/apps.py"))
        self.assertTrue(os.path.exists(f"{os.getcwd()}/dummy_generated_app/infrastructure/admin.py"))
        shutil.rmtree(f"{os.getcwd()}/dummy_generated_app")
