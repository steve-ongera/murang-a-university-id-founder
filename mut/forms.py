# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Category, LostID, IDReplacement, Payment
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class CustomUserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter your email'
    }))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'First Name'
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Last Name'
    }))
    registration_number = forms.CharField(
        max_length=20,
        help_text="Format: SC211/0530/2022 or ED511/0920/2022",
        validators=[RegexValidator(
            regex=r'^(SC|ED)\d{3}/\d{4}/\d{4}$',
            message="Registration number must follow the format SC211/0530/2022 or ED511/0920/2022"
        )],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registration Number'})
    )
    phone_number = forms.CharField(
        max_length=13,
        help_text="Format: +254XXXXXXXXX",
        validators=[RegexValidator(
            regex=r'^\+254\d{9}$',
            message="Phone number must be in format +254XXXXXXXXX"
        )],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
        help_text="Password must be at least 8 characters long."
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'registration_number', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)





class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'})
        }

class LostIDForm(forms.ModelForm):
    class Meta:
        model = LostID
        fields = '__all__'
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MU/YY/XXXXX'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course name'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'last_seen_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last seen location'}),
            'additional_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Provide any additional details'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'found_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location where ID was found'}),
            'finder_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Finder contact details'}),
            'id_front_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'id_back_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'additional_image1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'additional_image2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'additional_image3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class IDReplacementForm(forms.ModelForm):
    class Meta:
        model = IDReplacement
        fields = '__all__'
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MU/YY/XXXXX'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+254XXXXXXXXX'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course name'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Provide reason for ID replacement'}),
            'police_abstract': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'replacement_application': forms.Select(attrs={'class': 'form-select'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
            'transaction_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter transaction reference'}),
            'payment_status': forms.Select(attrs={'class': 'form-select'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'last_name', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'username': forms.FileInput(attrs={'class': 'form-control'}),
        }

class FoundIDForm(forms.ModelForm):
    class Meta:
        model = LostID
        fields = ['student_name', 'registration_number', 'course', 'found_location', 'finder_contact', 'id_front_image', 'id_back_image']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter registration number'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course name'}),
            'found_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter found location'}),
            'finder_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter finder contact'}),
            'id_front_image': forms.FileInput(attrs={'class': 'form-control'}),
            'id_back_image': forms.FileInput(attrs={'class': 'form-control'}),
        }