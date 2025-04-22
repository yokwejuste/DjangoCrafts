from django.http import HttpResponseForbidden
from acc_users.models import DeviceFingerprint


class DeviceValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_fp = request.session.get("device_fp")
        cookie_fp = request.COOKIES.get("device_fp")

        if session_fp and cookie_fp and session_fp != cookie_fp:
            return HttpResponseForbidden("Invalid device fingerprint")

        response = self.get_response(request)
        return response


class ClientHintsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.headers["Accept-CH"] = (
            "Sec-CH-UA,Sec-CH-UA-Platform,Sec-CH-UA-Platform-Version,"
            "Sec-CH-UA-Mobile,Sec-CH-UA-Arch,Sec-CH-UA-Bitness,"
            "Sec-CH-UA-Full-Version,Sec-CH-UA-Model"
        )
        response.headers["Critical-CH"] = "Sec-CH-UA,Sec-CH-UA-Platform"
        return response
