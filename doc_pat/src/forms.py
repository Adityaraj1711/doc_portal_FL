# from django import forms
# from .models import Patient
#
#
# class YourModelForm(forms.ModelForm):
#
#     follow_days = forms.IntegerField()
#
#     def save(self, commit=True):
#         follow_days = self.cleaned_data.get('follow_days', None)
#         # ...do something with extra_field here...
#         return super(YourModelForm, self).save(commit=commit)
#
#     class Meta:
#         model = Patient