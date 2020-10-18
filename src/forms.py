from django import forms

from .models import ProcedureForm

class ProcedureFormForm(forms.ModelForm):
    class Meta:
        model = ProcedureForm
        widgets = {
            'result': forms.TextInput(attrs={'placeholder': 'Did the patient get the result etc.'}),
        }