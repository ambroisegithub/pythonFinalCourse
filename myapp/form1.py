
# formModel

from django import forms
from .models1 import Logger
class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'