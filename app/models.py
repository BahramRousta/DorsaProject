from django.db import models


class Parameter(models.Model):
    """Model for parameters."""

    params = models.JSONField(default=dict)

    def __str__(self):
        return self.params
