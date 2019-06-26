from django.db import models
from django.db.models import CharField, DateField, IntegerField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class NotificacaoInfracao(models.Model):

    name = CharField(_("Nome do Radar"), blank=True, max_length=255)

    allowed_track_speed = models.IntegerField(_("Velocidade Permetida"),
        blank=True,
        null=True
    )

    considered_speed = models.IntegerField(_("Velocidade Considerada"),
        blank=True,
        null=True
    )

    considered_speed = models.DateField(_("Data"),
        blank=True,
        null=True
    )

    id = models.CharField(_("Id"),
        unique=True,
        blank=True,
        null=True
    )

    Infraction_identifier = models.CharField(_("Id da Infração"),
        unique=True,
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
