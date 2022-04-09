from django import forms
from django.forms.forms import Form
from django.views.generic.edit import FormView
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'phone', 'message']

    def save(self, commit=True):
      return super().save(commit=commit)