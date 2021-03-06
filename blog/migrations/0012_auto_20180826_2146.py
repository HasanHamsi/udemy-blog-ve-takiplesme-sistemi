# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-26 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180826_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='default/default-photo.jpg', help_text='Kapak Fotoğrafı Yükleyiniz', null=True, upload_to='blog', verbose_name='Resim'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='kategoriler',
            field=models.ManyToManyField(blank=True, related_name='blog', to='blog.Kategori'),
        ),
    ]
