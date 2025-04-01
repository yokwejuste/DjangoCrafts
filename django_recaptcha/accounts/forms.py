from captcha.fields import CaptchaField
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import (
    ReCaptchaV2Checkbox,
    ReCaptchaV2Invisible,
    ReCaptchaV3,
)


class ContactForm(forms.Form):
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class InvisibleForm(forms.Form):
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)


class V3Form(forms.Form):
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV3)


class DjangoCaptchaForm(forms.Form):
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
