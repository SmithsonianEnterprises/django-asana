# Generated by Django 2.1 on 2018-12-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djasana", "0015_alter_story_resource_subtype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="resource_subtype",
            field=models.CharField(
                blank=True,
                choices=[
                    ("comment", "comment"),
                    ("system", "system"),
                    ("added_to_tag", "added to tag"),
                    ("added_to_task", "added to task"),
                    ("added_to_project", "added to project"),
                    (
                        "all_dependencies_marked_complete",
                        "all dependencies marked complete",
                    ),
                    ("assigned", "assigned"),
                    ("attachment_added", "attachment added"),
                    ("attachment_liked", "attachment liked"),
                    ("comment_added", "comment added"),
                    ("comment_liked", "comment liked"),
                    ("dependency_added", "dependency added"),
                    ("dependency_due_date_changed", "dependency due date changed"),
                    ("dependency_marked_complete", "dependency marked complete"),
                    ("dependency_marked_incomplete", "dependency marked incomplete"),
                    ("dependency_removed", "dependency removed"),
                    ("dependent_added", "dependent added"),
                    ("dependent_removed", "dependent removed"),
                    ("description_changed", "description changed"),
                    ("due_date_changed", "due date changed"),
                    ("due_today", "due today"),
                    ("duplicate_merged", "duplicate merged"),
                    ("duplicated", "duplicated"),
                    ("enum_custom_field_changed", "enum custom field changed"),
                    ("follower_added", "follower added"),
                    ("liked", "liked"),
                    ("marked_complete", "marked complete"),
                    ("marked_duplicate", "marked duplicate"),
                    ("marked_incomplete", "marked incomplete"),
                    ("marked_today", "marked today"),
                    ("member_added", "member added"),
                    ("name_changed", "name changed"),
                    ("notes_changed", "notes changed"),
                    ("number_custom_field_changed", "number custom field changed"),
                    ("removed_from_project", "removed from project"),
                    ("removed_from_tag", "removed from tag"),
                    ("removed_from_task", "removed from task"),
                    ("section_changed", "section changed"),
                    ("starting_today", "starting today"),
                    ("unassigned", "unassigned"),
                ],
                max_length=48,
                null=True,
            ),
        ),
    ]
