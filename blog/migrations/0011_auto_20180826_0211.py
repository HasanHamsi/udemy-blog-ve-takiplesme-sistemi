# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-25 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180826_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='default/default-photo.jpg', help_text='Kapak Fotoğrafı Yükleyiniz', null=True, upload_to='', verbose_name='Resim'),
        ),
    ]
