# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attachment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "remote_id",
                    models.BigIntegerField(
                        db_index=True,
                        help_text="The id of this object in Asana.",
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("download_url", models.URLField()),
                ("host", models.CharField(choices=[("asana", "asana")], max_length=24)),
                ("permanent_url", models.URLField()),
                ("view_url", models.URLField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "remote_id",
                    models.BigIntegerField(
                        db_index=True,
                        help_text="The id of this object in Asana.",
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("archived", models.BooleanField()),
                ("color", models.CharField(max_length=16, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "current_status",
                    models.CharField(
                        choices=[
                            ("inbox", "inbox"),
                            ("upcoming", "upcoming"),
                            ("later", "later"),
                        ],
                        max_length=16,
                        null=True,
                    ),
                ),
                ("due_date", models.DateField(null=True)),
                ("layout", models.CharField(choices=[("list", "list")], max_length=16)),
                ("modified_at", models.DateTimeField()),
                ("notes", models.TextField()),
                ("public", models.BooleanField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Story",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "remote_id",
                    models.BigIntegerField(
                        db_index=True,
                        help_text="The id of this object in Asana.",
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("hearted", models.BooleanField(default=False)),
                ("num_hearts", models.SmallIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("target", models.BigIntegerField(db_index=True)),
                ("source", models.CharField(choices=[("web", "web")], max_length=16)),
                ("text", models.CharField(max_length=50)),
                (
                    "type",
                    models.CharField(
                        choices=[("comment", "comment"), ("system", "system")],
                        max_length=16,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "stories",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "remote_id",
                    models.BigIntegerField(
                        db_index=True,
                        help_text="The id of this object in Asana.",
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "remote_id",
                    models.BigIntegerField(
                        db_index=True,
                        help_text="The id of this object in Asana.",
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("hearted", models.BooleanField(default=False)),
                ("num_hearts", models.SmallIntegerField()),
                (
                    "assignee_status",
                    models.CharField(choices=[("inbox", "inbox")], max_length=16),
                ),
                ("completed", models.BooleanField()),
                ("completed_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("due_at", models.DateTimeField(null=True)),
                ("due_on", models.DateField(null=True)),
                ("modified_at", models.DateTimeField()),
                ("notes", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "remote_id",
                    models.BigIntegerField(
                        db_index=True,
                        help_text="The id of this object in Asana.",
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("organization_id", models.BigIntegerField(null=True)),
                ("organization_name", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "remote_id",
                    models.BigIntegerField(
                        db_index=True,
                        help_text="The id of this object in Asana.",
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "photo",
                    models.CharField(max_length=255, null=True, verbose_name="photo"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Workspace",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "remote_id",
                    models.BigIntegerField(
                        db_index=True,
                        help_text="The id of this object in Asana.",
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("is_organization", models.BooleanField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="user",
            name="workspaces",
            field=models.ManyToManyField(to="djasana.Workspace"),
        ),
        migrations.AddField(
            model_name="task",
            name="assignee",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assigned_tasks",
                to="djasana.User",
                to_field="remote_id",
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="followers",
            field=models.ManyToManyField(
                related_name="tasks_following", to="djasana.User"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="hearts",
            field=models.ManyToManyField(
                related_name="task_hearted", to="djasana.User"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="parent",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djasana.Task",
                to_field="remote_id",
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="projects",
            field=models.ManyToManyField(to="djasana.Project"),
        ),
        migrations.AddField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(to="djasana.Tag"),
        ),
        migrations.AddField(
            model_name="story",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="djasana.User",
                to_field="remote_id",
            ),
        ),
        migrations.AddField(
            model_name="story",
            name="hearts",
            field=models.ManyToManyField(
                related_name="story_hearted", to="djasana.User"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="followers",
            field=models.ManyToManyField(
                related_name="projects_following", to="djasana.User"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="members",
            field=models.ManyToManyField(to="djasana.User"),
        ),
        migrations.AddField(
            model_name="project",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects_owned",
                to="djasana.User",
                to_field="remote_id",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="djasana.Team",
                to_field="remote_id",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="workspace",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="djasana.Workspace",
                to_field="remote_id",
            ),
        ),
        migrations.AddField(
            model_name="attachment",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="djasana.Task",
                to_field="remote_id",
            ),
        ),
    ]
