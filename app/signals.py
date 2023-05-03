from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Parameter


@receiver(post_save, sender=Parameter)
@receiver(post_delete, sender=Parameter)
def user_cache_version(sender, **kwargs):
    # Update the cache version number to invalidate existing cache keys
    cache.delete('total_params_objects')
    cache.delete('history_params_objects')