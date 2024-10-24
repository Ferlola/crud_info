# Generated by Django 5.1.2 on 2024-10-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrudModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('update_description', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_date', models.JSONField(default=list)),
                ('updated_times', models.IntegerField()),
                ('location', models.JSONField(default=list)),
                ('update_location', models.JSONField(default=list)),
                ('machine', models.JSONField(default=list)),
                ('update_machine', models.JSONField(default=list)),
                ('network', models.JSONField(default=list)),
                ('update_network', models.JSONField(default=list)),
                ('ip', models.JSONField(default=list)),
                ('update_ip', models.JSONField(default=list)),
                ('hostname', models.JSONField(default=list)),
                ('update_hostname', models.JSONField(default=list)),
                ('IPAddr', models.JSONField(default=list)),
                ('update_IPAddr', models.JSONField(default=list)),
                ('ipconf', models.JSONField(default=list)),
                ('update_ipconf', models.JSONField(default=list)),
                ('ram_memory', models.JSONField(default=list)),
                ('update_ram_memory', models.JSONField(default=list)),
                ('ram_used', models.JSONField(default=list)),
                ('update_ram_used', models.JSONField(default=list)),
            ],
        ),
    ]
