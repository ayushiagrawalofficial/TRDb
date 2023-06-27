from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy


class Technology(models.Model):
    """Technology"""

    class Type(models.IntegerChoices):
        """Technology Type"""

        LANGUAGE = 0, gettext_lazy("Language")
        FRAMEWORK = 1, gettext_lazy("Framework")
        LIBRARY = 2, gettext_lazy("Library")
        PLATFORM = 3, gettext_lazy("Platform")
        TOOL = 4, gettext_lazy("Tool")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name=gettext_lazy("user"),
    )
    technology_type = models.SmallIntegerField(
        gettext_lazy("type"), choices=Type.choices, db_index=True
    )
    name = models.CharField(gettext_lazy("name"), max_length=255, unique=True)
    is_active = models.BooleanField(gettext_lazy("active"), default=True)
    created = models.DateTimeField(gettext_lazy("created"), auto_now_add=True)
    updated = models.DateTimeField(gettext_lazy("updated"), auto_now=True)

    class Mate:
        verbose_name = gettext_lazy("technology")
        verbose_name_plural = gettext_lazy("technologies")

    def clean(self):
        self.name = self.name.strip().title()


class StudyResource(models.Model):
    """Study Resource"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name=gettext_lazy("user"),
    )
    technology = models.ForeignKey(
        Technology,
        on_delete=Technology,
        related_name=gettext_lazy("technologies"),
        verbose_name=gettext_lazy("technology"),
    )
    title = models.CharField(gettext_lazy("title"), max_length=255)
    link = models.URLField(gettext_lazy("link"), unique=True)
    vote_count = models.IntegerField(gettext_lazy("vote count"), default=0)
    is_active = models.BooleanField(gettext_lazy("active"), default=True)
    created = models.DateTimeField(gettext_lazy("created"), auto_now_add=True)
    updated = models.DateTimeField(gettext_lazy("updated"), auto_now=True)

    class Mate:
        verbose_name = gettext_lazy("study resource")
        verbose_name_plural = gettext_lazy("study resources")


class Vote(models.Model):
    """Vote"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name=gettext_lazy("user"),
    )
    study_resource = models.ForeignKey(
        StudyResource,
        on_delete=Technology,
        related_name=gettext_lazy("votes"),
        verbose_name=gettext_lazy("study resource"),
    )
    created = models.DateTimeField(gettext_lazy("created"), auto_now_add=True)
    updated = models.DateTimeField(gettext_lazy("updated"), auto_now=True)

    class Mate:
        constraints = [
            models.UniqueConstraint(
                name="unique_vote",
                fields=["user", "study_resource"],
                deferrable=models.Deferrable.DEFERRED,
            ),
        ]
        verbose_name = gettext_lazy("vote")
        verbose_name_plural = gettext_lazy("votes")
