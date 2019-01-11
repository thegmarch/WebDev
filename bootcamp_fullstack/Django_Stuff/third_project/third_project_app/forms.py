from django import forms
from django.core import validators
from thrid_project_app.models import SignUpForm
from django.forms import ModelForm


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter you email again!')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("make sure emails match")

class SUForm(ModelForm):
    class Meta:
        model = SignUp_Form
        fields = ['name','email']
