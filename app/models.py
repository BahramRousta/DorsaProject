from django.db import models


class Parameter(models.Model):
    """Model for parameters."""

    a = models.FloatField()
    b = models.FloatField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.a} + {self.b} = {self.total}"