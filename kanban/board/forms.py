from django import forms
from .models import ticket

class ticketform(forms.ModelForm):
  class Meta:
    model=ticket
    fields="__all__"