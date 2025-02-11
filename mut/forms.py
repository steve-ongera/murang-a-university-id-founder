# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    registration_number = forms.CharField(
        max_length=20,
        help_text="Format: MU/YY/XXXXX"
    )
    phone_number = forms.CharField(
        max_length=13,
        help_text="Format: +254XXXXXXXXX"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 
                 'registration_number', 'phone_number', 'password1', 'password2')

    def clean_registration_number(self):
        reg_no = self.cleaned_data.get('registration_number')
        if not reg_no.startswith('MU/'):
            raise forms.ValidationError("Registration number must start with 'MU/'")
        return reg_no

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.startswith('+254'):
            raise forms.ValidationError("Phone number must start with '+254'")
        return phone

class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
