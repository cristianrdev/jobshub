# Generated by Django 3.1.7 on 2021-06-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='match',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]