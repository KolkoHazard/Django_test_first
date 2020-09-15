from django import forms
from contact.models import Contact


class FormName(forms.ModelForm):
    class Meta:
        model=Contact
        fields= '__all__'
