from django.db import models


class CustomModel(models.Model):
    custom_field = models.TextField()
