# Generated by Django 3.0 on 2023-10-11 08:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("oc_lettings_site", "0002_auto_20231010_1710"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name="Profile",
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name="Profile",
                    table="profiles_profile",
                ),
            ],
        ),
    ]
