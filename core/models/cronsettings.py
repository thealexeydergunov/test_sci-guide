from django.db import models
from .choices import STATUS_CRON


class CronSettings(models.Model):
    code = models.CharField(max_length=200)
    status_cron = models.PositiveSmallIntegerField(
        choices=STATUS_CRON.CHOICES,
        default=STATUS_CRON.WAIT
    )
