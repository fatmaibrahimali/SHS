from django import forms
from .models import UserVital




class UserVitalForm(forms.Form):
    class Meta:
        model = UserVital
        fields = '__all__'
        exclude = ('user')