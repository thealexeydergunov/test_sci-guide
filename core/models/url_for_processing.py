from django.db import models
from .choices import STATUS_URL_PROCESSING
from datetime import datetime


class URLForProcessing(models.Model):
    url = models.URLField()
    timeshift = models.DurationField(
        blank=True,
        null=True,
        help_text='After how many time process parsing this url will be started. '
                  'Enter empty value if you want fast start processing.'
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_URL_PROCESSING.CHOICES,
        default=STATUS_URL_PROCESSING.WAIT,
        verbose_name='Operation status'
    )
    start_processing = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.url

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.start_processing = datetime.now() + self.timeshift
        return super().save(force_insert, force_update, using, update_fields)
