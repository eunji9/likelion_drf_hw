# Generated by Django 5.2.3 on 2025-07-02 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='name',
            new_name='title',
        ),
    ]
