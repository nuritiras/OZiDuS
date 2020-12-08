# Generated by Django 3.1.4 on 2020-12-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ozildata', '0012_auto_20201206_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zildata',
            name='xzilgun',
            field=models.SmallIntegerField(choices=[[0, 'Pazartesi'], [1, 'Salı'], [2, 'Çarşamba'], [3, 'Perşembe'], [4, 'Cuma'], [5, 'Cumartesi'], [6, 'Pazar']], default=0, verbose_name='Günü Seçin'),
        ),
    ]