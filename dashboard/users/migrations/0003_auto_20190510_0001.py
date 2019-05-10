# Generated by Django 2.0.13 on 2019-05-10 00:01

import dashboard.users.utils.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190509_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='matricula',
        ),
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(help_text='Por favor, entre com um CPFseguindo o formato: XXX.XXX.XXX-XX', max_length=14, unique=True, validators=[dashboard.users.utils.validators.validate_cpf]),
        ),
    ]
