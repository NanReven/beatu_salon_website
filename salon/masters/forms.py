from django import forms

from .models import Weekday


class MasterForm(forms.ModelForm):
    weekend = forms.ModelMultipleChoiceField(queryset=Weekday.objects, widget=forms.CheckboxSelectMultiple())
