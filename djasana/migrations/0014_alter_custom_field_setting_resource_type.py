# Generated by Django 2.1.3 on 2018-12-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djasana", "0013_renames_custom_field_setting"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customfieldsetting",
            name="resource_type",
            field=models.CharField(
                blank=True, default="custom_field_setting", max_length=24, null=True
            ),
        ),
    ]
