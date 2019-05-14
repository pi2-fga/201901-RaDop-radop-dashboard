from django.db import models
from django.db.models import CharField, FloatField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class Radar(models.Model):

    name = CharField(_("Nome do Radar"), blank=True, max_length=255)

    identificacao = models.CharField(_("Identificação do Radar"),
        max_length=10,
        unique=True,
        blank=True,
        null=True
    )

    longitude = models.FloatField(_("Longitude"),
        blank=True,
        null=True
    )

    latitude = models.FloatField(_("Latitude"),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Radar")
        verbose_name_plural = _("Radares")

    def get_absolute_url(self):
        return reverse("radar:detail", kwargs={"name": self.name})

    
