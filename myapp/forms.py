from django import forms
from django.forms.widgets import NumberInput
SHIFTS = (
    ('1','morning'),
    ('2','afternoon'),
    ('3','Evening'),
    
)
Employees = (
    ('1','manager'),
    ('2','cachier'),
    ('3','chief'),
    
)
class InputForm(forms.Form):
    
    first_Name = forms.CharField(max_length=60)
    last_Name = forms.CharField(max_length=70)
    Email = forms.EmailField()
    Date =forms.DateField(widget= NumberInput(attrs={'type': 'date'}))
    shift = forms.ChoiceField(choices=SHIFTS)
    files = forms.FileField()
    MyfavouriteEmployes = forms.ChoiceField(widget=forms.RadioSelect,choices=Employees)
    TextArea = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    time_log = forms.TimeField()
    

    # def __str__(self):
    #     return self.firstName + ' ' + self.lastName