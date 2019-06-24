from django.db import models
from django.utils.translation import ugettext_lazy as _


class Penalty(models.Model):
    MEDIUM = 'MEDIA'
    SEVERE = 'SEVERE'
    EX_SEVERE = 'EXTREME SEVERE'

    LEVEL_OPTIONS = (
        (MEDIUM, 'Média'),
        (SEVERE, 'Grave'),
        (EX_SEVERE, 'Gravíssima')
    )

    level = models.CharField(
        max_length=14,
        choices=LEVEL_OPTIONS,
        default=MEDIUM,
    )

    points = models.IntegerField(
        default=3,
    )

    value = models.FloatField(
        default=130.16,
    )

    class Meta:
        verbose_name = _('Multa')
        verbose_name_plural = _('Multas')

    def __str__(self):
        if self.level == self.MEDIUM:
            return f'Penalidade {self.LEVEL_OPTIONS[0][1]}'
        elif self.level == self.SEVERE:
            return f'Penalidade {self.LEVEL_OPTIONS[1][1]}'
        elif self.level == self.EX_SEVERE:
            return f'Penalidade {self.LEVEL_OPTIONS[2][1]}'


class Notification(models.Model):
    INFRACTION = 'INFRACAO'
    FEASIBLE = 'POSSIVEL'

    AC = 'AC'
    AL = 'AL'
    AP = 'AP'
    AM = 'AM'
    BA = 'BA'
    CE = 'CE'
    DF = 'DF'
    ES = 'ES'
    GO = 'GO'
    MA = 'MA'
    MT = 'MT'
    MS = 'MS'
    MG = 'MG'
    PA = 'PA'
    PB = 'PB'
    PR = 'PR'
    PE = 'PE'
    PI = 'PI'
    RJ = 'RJ'
    RN = 'RN'
    RS = 'RS'
    RO = 'RO'
    RR = 'RR'
    SC = 'SC'
    SP = 'SP'
    SE = 'SE'
    TO = 'TO'


    NOTIFICATION_OPTIONS = (
        (INFRACTION, 'Infração'),
        (FEASIBLE, 'Possível Acidente')
    )

    STATE_OPTIONS = (
        (AC, AC),
        (AL, AL),
        (AP, AP),
        (AM, AM),
        (BA, BA),
        (CE, CE),
        (DF, DF),
        (ES, ES),
        (GO, GO),
        (MA, MA),
        (MT, MT),
        (MS, MS),
        (MG, MG),
        (PA, PA),
        (PB, PB),
        (PR, PR),
        (PE, PE),
        (PI, PI),
        (RJ, RJ),
        (RN, RN),
        (RS, RS),
        (RO, RO),
        (RR, RR),
        (SC, SC),
        (SP, SP),
        (SE, SE),
        (TO, TO)
    )

    allowed_track_speed = models.IntegerField(
        default=0,
        blank=True,
    )

    considered_speed = models.IntegerField(
        default=0,
        blank=True,
    )

    crash_feasability = models.FloatField(
        default=0.0,
        blank=True,
    )

    date = models.CharField(
        max_length=10,
        blank=True,
    )

    infraction_identifier = models.CharField(
        max_length=36,
    )

    identifier = models.CharField(
        max_length=36,
    )

    notification_type = models.CharField(
        max_length=17,
        choices=NOTIFICATION_OPTIONS,
        default=INFRACTION,
        blank=True,
    )

    penalty = models.ForeignKey(
        'Penalty',
        on_delete=models.CASCADE,
        blank=True,
    )

    read_speed = models.IntegerField(
        default=0,
        blank=True,
    )

    time = models.CharField(
        max_length=8,
        blank=True,
    )

    vehicle_brand = models.CharField(
        max_length=200,
        blank=True,
    )

    vehicle_chassi = models.CharField(
        max_length=200,
        blank=True,
    )

    vehicle_city = models.CharField(
        max_length=500,
        blank=True,
    )

    vehicle_color = models.CharField(
        max_length=200,
        blank=True,
    )

    vehicle_model = models.CharField(
        max_length=200,
        blank=True,
    )

    vehicle_plate = models.CharField(
        max_length=7,
        blank=True,
    )

    vehicle_state = models.CharField(
        max_length=2,
        choices=STATE_OPTIONS,
        blank=True,
    )

    vehicle_status = models.CharField(
        max_length=200,
        blank=True,
    )

    vehicle_year = models.CharField(
        max_length=4,
        blank=True,
    )

    class Meta:
        verbose_name = _("Notificação")
        verbose_name_plural = _("Notificações")

    def __str__(self):
        return _(f'Infração N {self.name}')
