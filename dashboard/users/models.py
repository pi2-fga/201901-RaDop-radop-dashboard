from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .utils.validators import validate_cpf


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
        help_text=_("DD/MM/AAAA"),
        blank=False,
        null=True
    )

    cpf = models.CharField(
        help_text=_("Por favor, entre com um CPF" +
                    "seguindo o formato: XXX.XXX.XXX-XX"),
        unique=True,
        blank=True,
        null=True,
        validators=[validate_cpf],
        max_length=14,
    )

    matricula = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    
