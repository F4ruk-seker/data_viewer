from django.core.exceptions import ValidationError
from django.db import models


class ChartSetting(models.Model):

    def save(self, *args, **kwargs):
        if not self.pk and ChartSetting.objects.count() > 0:
            raise ValidationError('Only one instance is allowed.')
        super().save(*args, **kwargs)

