from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, UserProfile




class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2', 'national_id', 'phone')




class Login_Form(forms.ModelForm):
    username = forms.CharField(label='username', required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ('username', 'password')
        
    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            return {'username':username, 'password':password}
        raise forms.ValidationError("Invalid login")
            
      
            
class UserProfileForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user','birth_date', 'sex')
