from django.contrib import admin
from .models import DeviceFingerprint

@admin.register(DeviceFingerprint)
class DeviceFingerprintAdmin(admin.ModelAdmin):
    list_display = ['fingerprint', 'platform', 'language', 'created_at']
    list_filter = ['platform', 'language']
    search_fields = ['fingerprint', 'user_agent']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
