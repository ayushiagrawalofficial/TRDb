from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from resources.models import StudyResource, Vote


@receiver(post_save, sender=Vote)
def increment_vote_count_receiver(sender, instance, created, **kwargs):
    """Increment Vote Count Receiver"""
    obj = StudyResource.objects.get(pk=instance.study_resource.pk)
    obj.vote_count += 1
    obj.save()


@receiver(post_delete, sender=Vote)
def decrement_vote_count_receiver(sender, instance, **kwargs):
    """Decrement Vote Count Receiver"""
    obj = StudyResource.objects.get(pk=instance.study_resource.pk)
    obj.vote_count -= 1
    obj.save()
