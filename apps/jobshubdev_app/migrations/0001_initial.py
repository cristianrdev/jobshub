# Generated by Django 3.1.7 on 2021-06-14 08:14

import apps.jobshubdev_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=45)),
                ('icon_link_language', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('developer', models.ManyToManyField(related_name='developer_language', to='login_app.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=45)),
                ('icon_link_framework', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('developer', models.ManyToManyField(related_name='developer_framework', to='login_app.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_bio', models.CharField(blank=True, max_length=255, validators=[apps.jobshubdev_app.models.ValidarLongitudMinima])),
                ('github_link', models.CharField(blank=True, max_length=255, validators=[apps.jobshubdev_app.models.ValidarGithub])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_biography', to='login_app.developer')),
            ],
        ),
    ]
