# Generated by Django 3.1.7 on 2021-06-11 00:20

import apps.login_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[apps.login_app.models.ValidarLongitudMinima])),
                ('last_name', models.CharField(max_length=30, validators=[apps.login_app.models.ValidarLongitudMinima])),
                ('email', models.CharField(max_length=30, validators=[apps.login_app.models.validarEmail])),
                ('address_name', models.CharField(max_length=50)),
                ('address_number', models.CharField(max_length=8, validators=[apps.login_app.models.ValidarLongitudMinima])),
                ('address_detail', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(max_length=100, validators=[apps.login_app.models.ValidarLongitudPassword])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=45, validators=[apps.login_app.models.ValidarLongitudMinima])),
                ('first_name', models.CharField(max_length=45, validators=[apps.login_app.models.ValidarLongitudMinima])),
                ('last_name', models.CharField(max_length=45, validators=[apps.login_app.models.ValidarLongitudMinima])),
                ('email', models.CharField(max_length=50, validators=[apps.login_app.models.validarEmail])),
                ('address_name', models.CharField(max_length=50)),
                ('address_number', models.CharField(max_length=8, validators=[apps.login_app.models.ValidarLongitudMinima])),
                ('address_detail', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(max_length=100, validators=[apps.login_app.models.ValidarLongitudPassword])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
