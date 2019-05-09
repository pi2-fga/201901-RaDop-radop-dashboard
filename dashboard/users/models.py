from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Nome do usuário"), blank=True, max_length=255)

    gender = models.CharField(
        _('Gender'),
        choices=(
            (("Masculino"), _("Masculino")),
            (("Feminino"), _("Feminino")),
        ),
        blank=False,
        max_length=10,
        null=True
    )

    birthday = models.DateField(
        _('Birthday'),
        help_text=_("xx/xx/xxxx"),
        blank=False,
        null=True
    )

    cpf = models.CharField(
        help_text=_("Por favor, entre com um CPF" +
                    "seguindo o formato: XXX.XXX.XXX-XX"),
        unique=True,
        max_length=14,
        default='000.000.000-00',
    )

    matricula = models.CharField(
        unique=True,
        max_length=7,
        default='00'
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
