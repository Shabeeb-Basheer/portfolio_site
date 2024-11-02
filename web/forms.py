
# web/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact
from django.forms import widgets

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control fw-normal w-full leading-7 contact-form-control ", "placeholder": "Your Name"}),
            "email": widgets.TextInput(attrs={"class": "required form-control fw-normal w-full leading-7 contact-form-control ", "placeholder": "Your Email"}),
            "phone": widgets.TextInput(attrs={"class": "required form-control fw-normal w-full leading-7 contact-form-control ", "placeholder": "Your Phone"}),
            "subject": widgets.TextInput(attrs={"class": "required form-control fw-normal w-full leading-7 contact-form-control ", "placeholder": "Your Subject"}),
            "message": widgets.Textarea(attrs={"class": "required form-control fw-normal w-full leading-7 contact-form-control ","placeholder": "Type Your Message","id":"message"}),
        }