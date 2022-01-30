# Generated by Django 2.1.11 on 2019-10-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djasana", "0019_adds_project_is_template"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="default_view",
            field=models.CharField(
                blank=True,
                choices=[
                    ("board", "board"),
                    ("calendar", "calendar"),
                    ("list", "list"),
                    ("timeline", "timeline"),
                ],
                max_length=16,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="layout",
            field=models.CharField(
                choices=[
                    ("board", "board"),
                    ("calendar", "calendar"),
                    ("list", "list"),
                    ("timeline", "timeline"),
                ],
                max_length=16,
            ),
        ),
    ]
