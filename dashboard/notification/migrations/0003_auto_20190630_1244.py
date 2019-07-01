# Generated by Django 2.0.13 on 2019-06-30 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20190627_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='identifier',
            field=models.CharField(max_length=36),
        ),
        migrations.AlterField(
            model_name='notification',
            name='infraction_identifier',
            field=models.CharField(max_length=36),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='level',
            field=models.CharField(blank=True, choices=[('MEDIA', 'Média'), ('SEVERE', 'Grave'), ('EXTREME SEVERE', 'Gravíssima')], default='MEDIA', max_length=14),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='points',
            field=models.IntegerField(blank=True, default=3),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='value',
            field=models.FloatField(blank=True, default=130.16),
        ),
    ]