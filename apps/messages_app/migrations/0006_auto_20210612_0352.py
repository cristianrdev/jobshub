# Generated by Django 3.1.7 on 2021-06-12 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messages_app', '0005_messagedev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagedev',
            old_name='message_content',
            new_name='message_dev_content',
        ),
    ]