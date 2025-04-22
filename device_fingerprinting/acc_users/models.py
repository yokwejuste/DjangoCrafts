from django.db import models
import uuid

class DeviceFingerprint(models.Model):
    fingerprint = models.CharField(max_length=255, unique=True)
    user_agent = models.TextField()
    language = models.CharField(max_length=50)
    platform = models.CharField(max_length=100)
    screen_resolution = models.CharField(max_length=50)
    timezone = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(null=True)
    browser_plugins = models.TextField(null=True)
    hardware_concurrency = models.IntegerField(null=True)
    device_memory = models.FloatField(null=True)
    cpu_cores = models.IntegerField(null=True)
    total_memory = models.FloatField(null=True)
    performance_metrics = models.TextField(null=True)
    color_depth = models.IntegerField(null=True)
    pixel_ratio = models.FloatField(null=True)
    touch_support = models.BooleanField(default=False)
    canvas_hash = models.CharField(max_length=255, null=True)
    webgl_vendor = models.CharField(max_length=255, null=True)
    webgl_renderer = models.CharField(max_length=255, null=True)
    audio_hash = models.CharField(max_length=255, null=True)
    connection_type = models.CharField(max_length=50, null=True)
    connection_speed = models.CharField(max_length=50, null=True)
    battery_level = models.FloatField(null=True)
    battery_charging = models.BooleanField(null=True)
    do_not_track = models.CharField(max_length=20, null=True)
    mac_address = models.CharField(max_length=100, null=True)  # Added MAC address field
    created_at = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)
    browser_id = models.CharField(max_length=255, db_index=True, default=uuid.uuid4, null=True)

    class Meta:
        ordering = ['-last_seen']
        indexes = [
            models.Index(fields=['fingerprint']),
            models.Index(fields=['browser_id']),
        ]

    def __str__(self):
        return f"Fingerprint: {self.fingerprint} - {self.created_at}"

    def has_significant_changes(self, new_data):
        """Check if there are significant changes in the fingerprint data."""
        if 'ip_address' in new_data and self.ip_address != new_data['ip_address']:
            return True
        if 'mac_address' in new_data and self.mac_address != new_data['mac_address']:
            return True

        significant_fields = [
            ('user_agent', 'userAgent'),
            ('platform', 'platform'),
            ('cpu_cores', 'cpuCores'),
            ('total_memory', 'totalMemory'),
            ('hardware_concurrency', 'hardwareConcurrency'),
            ('device_memory', 'deviceMemory'),
            ('screen_resolution', 'screenResolution'),
            ('color_depth', 'colorDepth'),
            ('pixel_ratio', 'pixelRatio'),
            ('webgl_vendor', 'webglVendor'),
            ('webgl_renderer', 'webglRenderer'),
        ]
        
        for model_field, data_field in significant_fields:
            old_value = getattr(self, model_field)
            new_value = new_data.get(data_field)
            
            if new_value is not None and old_value != new_value:
                return True
        
        return False
