from django.db import models


class Log(models.Model):
    log = models.TextField(blank=True, null=True)
