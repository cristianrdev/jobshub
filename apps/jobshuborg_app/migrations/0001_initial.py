# Generated by Django 3.1.7 on 2021-06-14 04:30

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '__first__'),
        ('jobshubdev_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_title', models.CharField(max_length=45)),
                ('position_description', models.CharField(max_length=255)),
                ('state_position', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position_filled_by', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.expressions.Case, related_name='developer_position', to='login_app.developer')),
                ('position_framework', models.ManyToManyField(blank=True, related_name='framework_position', to='jobshubdev_app.Framework')),
                ('position_language', models.ManyToManyField(blank=True, related_name='language_position', to='jobshubdev_app.Language')),
                ('position_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_position', to='login_app.organization')),
            ],
        ),
    ]
