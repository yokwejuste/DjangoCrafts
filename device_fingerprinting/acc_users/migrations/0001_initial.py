# Generated by Django 5.2 on 2025-04-22 12:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceFingerprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint', models.CharField(max_length=255, unique=True)),
                ('user_agent', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=100)),
                ('screen_resolution', models.CharField(max_length=50)),
                ('timezone', models.CharField(max_length=100)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('browser_plugins', models.TextField(null=True)),
                ('hardware_concurrency', models.IntegerField(null=True)),
                ('device_memory', models.FloatField(null=True)),
                ('cpu_cores', models.IntegerField(null=True)),
                ('total_memory', models.FloatField(null=True)),
                ('performance_metrics', models.TextField(null=True)),
                ('color_depth', models.IntegerField(null=True)),
                ('pixel_ratio', models.FloatField(null=True)),
                ('touch_support', models.BooleanField(default=False)),
                ('canvas_hash', models.CharField(max_length=255, null=True)),
                ('webgl_vendor', models.CharField(max_length=255, null=True)),
                ('webgl_renderer', models.CharField(max_length=255, null=True)),
                ('audio_hash', models.CharField(max_length=255, null=True)),
                ('connection_type', models.CharField(max_length=50, null=True)),
                ('connection_speed', models.CharField(max_length=50, null=True)),
                ('battery_level', models.FloatField(null=True)),
                ('battery_charging', models.BooleanField(null=True)),
                ('do_not_track', models.CharField(max_length=20, null=True)),
                ('mac_address', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_seen', models.DateTimeField(auto_now=True)),
                ('browser_id', models.CharField(db_index=True, default=uuid.uuid4, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-last_seen'],
                'indexes': [models.Index(fields=['fingerprint'], name='acc_users_d_fingerp_ab785b_idx'), models.Index(fields=['browser_id'], name='acc_users_d_browser_b6c660_idx')],
            },
        ),
    ]
