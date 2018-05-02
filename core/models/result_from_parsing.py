from django.db import models


class ResultFromParsing(models.Model):
    url = models.OneToOneField(
        'core.URLForProcessing',
        on_delete=models.CASCADE,
        verbose_name='URL'
    )
    title = models.CharField(
        max_length=256,
        blank=True
    )
    charset = models.CharField(
        max_length=10,
        blank=True
    )
    h1 = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return 'Results {}'.format(self.url.url)
