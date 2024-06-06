from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from auditlog.models import LogEntry
from .models import Monografia

@receiver(post_save, sender=Monografia)
def monografia_post_save(sender, instance, created, kwargs):
    if created:
        action = LogEntry.Action.CREATE
    else:
        action = LogEntry.Action.UPDATE

    log_entry = LogEntry.objects.create(
        content_type=instance.get_content_type(),
        object_pk=instance.pk,
        object_repr=str(instance),
        action=action,
        changes="Custom changes description",
    )

@receiver(post_delete, sender=Monografia)
def monografia_post_delete(sender, instance, kwargs):
    log_entry = LogEntry.objects.create(
        content_type=instance.get_content_type(),
        object_pk=instance.pk,
        object_repr=str(instance),
        action=LogEntry.Action.DELETE,
        changes="Custom changes description",
    )