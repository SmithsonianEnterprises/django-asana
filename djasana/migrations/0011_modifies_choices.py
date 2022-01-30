# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djasana", "0010_short_webhook_secret"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="color",
            field=models.CharField(
                blank=True,
                choices=[
                    ("dark-pink", "dark-pink"),
                    ("dark-green", "dark-green"),
                    ("dark-blue", "dark-blue"),
                    ("dark-red", "dark-red"),
                    ("dark-teal", "dark-teal"),
                    ("dark-brown", "dark-brown"),
                    ("dark-orange", "dark-orange"),
                    ("dark-purple", "dark-purple"),
                    ("dark-warm-gray", "dark-warm-gray"),
                    ("light-pink", "light-pink"),
                    ("light-green", "light-green"),
                    ("light-blue", "light-blue"),
                    ("light-red", "light-red"),
                    ("light-teal", "light-teal"),
                    ("light-yellow", "light-yellow"),
                    ("light-orange", "light-orange"),
                    ("light-purple", "light-purple"),
                    ("light-warm-gray", "light-warm-gray"),
                ],
                max_length=16,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="layout",
            field=models.CharField(
                choices=[("board", "board"), ("list", "list")], max_length=16
            ),
        ),
    ]
