from django import forms
from django.forms.forms import Form
from django.views.generic.edit import FormView
from .models import *

class SubscribeForm(forms.ModelForm):
  class Meta:
    model = Subscriber
    fields = ['email']

    def save(self, commit=True):
      return super().save(commit=commit)