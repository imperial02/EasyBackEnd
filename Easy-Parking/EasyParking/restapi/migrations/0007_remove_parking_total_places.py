# Generated by Django 2.1.2 on 2018-11-22 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0006_remove_section_total_places'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parking',
            name='total_places',
        ),
    ]
