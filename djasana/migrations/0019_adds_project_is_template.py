# Generated by Django 2.1.7 on 2019-08-30 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djasana", "0018_adds_custom_field_is_global_to_workspace"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="is_template",
            field=models.BooleanField(default=False),
        ),
    ]
