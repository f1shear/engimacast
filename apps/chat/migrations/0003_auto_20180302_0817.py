# Generated by Django 2.0 on 2018-03-02 08:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0002_chatroommodel_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatroommodel',
            old_name='created_on',
            new_name='created_at',
        ),
    ]
