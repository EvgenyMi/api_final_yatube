# Generated by Django 3.2.16 on 2023-01-22 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230122_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='descriptoin',
            new_name='description',
        ),
    ]