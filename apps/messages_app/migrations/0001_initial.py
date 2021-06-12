# Generated by Django 3.1.7 on 2021-06-12 04:24

import apps.messages_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0004_developer_skills_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_content', models.CharField(blank=True, max_length=8, validators=[apps.messages_app.models.ValidarLongitudMinima])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_message', to='login_app.organization')),
                ('message_to_developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='developer_message', to='login_app.developer')),
            ],
        ),
    ]
