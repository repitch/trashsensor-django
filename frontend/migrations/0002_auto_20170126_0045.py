# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-25 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': '\u0421\u0435\u043d\u0441\u043e\u0440', 'verbose_name_plural': '\u0421\u0435\u043d\u0441\u043e\u0440\u044b'},
        ),
        migrations.AddField(
            model_name='sensor',
            name='datetime_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='write_key',
            field=models.CharField(max_length=256, null=True, verbose_name='\u041a\u043b\u044e\u0447 \u0437\u0430\u043f\u0438\u0441\u0438'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(blank=True, max_length=256, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='elevation',
            field=models.CharField(blank=True, max_length=128, verbose_name='\u0412\u044b\u0441\u043e\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='last_entry_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='id \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u043e\u0442\u0447\u0435\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(blank=True, max_length=128, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='ranking',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0420\u0430\u043d\u043a'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id \u043d\u0430 thingspeak'),
        ),
    ]