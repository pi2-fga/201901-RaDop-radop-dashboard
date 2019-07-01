from django.db import models
from django.db.models import CharField, IntegerField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField
from dashboard.radar.utils import RADOP_API
import requests


class Radar(models.Model):

    name = CharField(_("Nome do Radar"), blank=True, max_length=255)

    identificacao = models.IntegerField(_("Identificação do Radar"),
        unique=True,
        blank=True,
        null=True
    )

    position = GeopositionField(
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

    def save(self):
        user_id = 1
        radar_name = self.name
        latitude = float(self.position.latitude)
        longitude = float(self.position.longitude)

        package = {
            'user_id': user_id,
            'name': radar_name,
            'latitude': latitude,
            'longitude': longitude
        }

        response = requests.post(url=f'{RADOP_API}/radars', json=package)

        if response.status_code == 200:
            super(Radar, self).save()
