# Generated by Django 3.1.7 on 2021-06-12 07:22

import apps.messages_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_developer_skills_number'),
        ('messages_app', '0004_auto_20210612_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageDev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_content', models.CharField(blank=True, max_length=255, validators=[apps.messages_app.models.ValidarLongitudMinima])),
                ('readed_by_organization', models.BooleanField(default=False, max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='developer_message_dev', to='login_app.developer')),
                ('message_to_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_message_dev', to='login_app.organization')),
            ],
        ),
    ]