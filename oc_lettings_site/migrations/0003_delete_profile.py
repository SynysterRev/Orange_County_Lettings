# Generated by Django 3.0 on 2025-04-16 09:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('oc_lettings_site', '0002_auto_20250416_1138'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Profile',
                ),
            ]
        )
    ]
