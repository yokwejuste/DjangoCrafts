from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from django.db import transaction
import json
import hashlib
import requests
from .models import DeviceFingerprint
import logging

logger = logging.getLogger(__name__)


def get_public_ip():
    """Get the real public IP address."""
    try:
        services = [
            "https://api.ipify.org?format=json",
            "https://api.ip.sb/ip",
            "https://api64.ipify.org?format=json",
        ]

        for service in services:
            try:
                response = requests.get(service, timeout=5)
                if response.status_code == 200:
                    if service.endswith("json"):
                        return response.json()["ip"]
                    return response.text.strip()
            except:
                continue

        return None
    except Exception as e:
        logger.error(f"Error getting public IP: {str(e)}")
        return None


@ensure_csrf_cookie
def index(request):
    return render(request, "index.html")


@require_http_methods(["POST"])
def save_fingerprint(request):
    try:
        data = json.loads(request.body)
        logger.debug(f"Received fingerprint data: {data}")

        ip_address = get_public_ip()
        if not ip_address:
            return JsonResponse(
                {"status": "error", "message": "Could not determine public IP address"},
                status=400,
            )

        normalized_data = {
            "fingerprint": data.get("fingerprint", ""),
            "user_agent": data.get("userAgent") or data.get("user_agent", "Unknown"),
            "language": data.get("language", ""),
            "platform": data.get("platform", "Unknown"),
            "screen_resolution": data.get("screenResolution") or data.get("screen_resolution", "Unknown"),
            "timezone": data.get("timezone", ""),
            "ip_address": ip_address,
            "mac_address": data.get("macAddress") or data.get("mac_address", ""),
            "hardware_concurrency": data.get("hardwareConcurrency") or data.get("hardware_concurrency"),
            "device_memory": data.get("deviceMemory") or data.get("device_memory"),
            "color_depth": data.get("colorDepth") or data.get("color_depth"),
            "pixel_ratio": data.get("pixelRatio") or data.get("pixel_ratio"),
            "touch_support": data.get("touchSupport", False),
            "canvas_hash": data.get("canvasHash", ""),
            "webgl_vendor": data.get("webglVendor", ""),
            "webgl_renderer": data.get("webglRenderer", ""),
            "audio_hash": data.get("audioHash", ""),
            "connection_type": data.get("connectionType", ""),
            "connection_speed": data.get("connectionSpeed", ""),
            "battery_level": data.get("batteryLevel"),
            "battery_charging": data.get("batteryCharging", False),
            "do_not_track": data.get("doNotTrack", False)
        }
        
        stable_components = {
            "user_agent": normalized_data["user_agent"],
            "platform": normalized_data["platform"],
            "screen_resolution": normalized_data["screen_resolution"],
            "hardware_concurrency": normalized_data["hardware_concurrency"],
            "device_memory": normalized_data["device_memory"],
            "color_depth": normalized_data["color_depth"],
            "pixel_ratio": normalized_data["pixel_ratio"],
            "mac_address": normalized_data["mac_address"],
        }

        browser_id = hashlib.sha256(
            json.dumps(stable_components, sort_keys=True).encode()
        ).hexdigest()

        with transaction.atomic():
            existing_fingerprint = DeviceFingerprint.objects.filter(
                browser_id=browser_id
            ).first()

            if existing_fingerprint:
                if not existing_fingerprint.has_significant_changes(normalized_data):
                    existing_fingerprint.save(update_fields=["last_seen"])
                    return JsonResponse({
                        "status": "success",
                        "id": existing_fingerprint.id,
                        "ip_address": ip_address,
                        "mac_address": normalized_data["mac_address"],
                        "message": "Browser fingerprint unchanged",
                        "is_new": False,
                    })

            fingerprint = DeviceFingerprint.objects.create(
                **normalized_data,
                browser_id=browser_id
            )

            return JsonResponse({
                "status": "success",
                "id": fingerprint.id,
                "ip_address": ip_address,
                "message": "New browser fingerprint saved",
                "is_new": True,
            })

    except json.JSONDecodeError:
        logger.error("Invalid JSON data received")
        return JsonResponse(
            {"status": "error", "message": "Invalid JSON data"}, status=400
        )
    except Exception as e:
        logger.error(f"Error saving fingerprint: {str(e)}")
        return JsonResponse(
            {"status": "error", "message": "Server error while saving fingerprint"},
            status=500,
        )
