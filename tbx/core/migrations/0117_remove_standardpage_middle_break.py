# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0116_delete_marketing_landing_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standardpage',
            name='middle_break',
        ),
    ]
