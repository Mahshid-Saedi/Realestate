from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکرار کلمه عبور', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('پسور ها درست نیستند')
        return cd['password2']

    def save(self, commit = True):
        user =super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='you can change password using <a href = \"../password/\">this form</a>')

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'password', 'last_login')


class UserRegisterationForm(forms.Form):
    email = forms.EmailField(label='ایمیل')
    phone_number = forms.CharField(max_length=11, label='تلفن')
    full_name = forms.CharField(label='نام و نام خانوادگی')
    password = forms.CharField(label='کلمه عبور' , widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email = email).exists()
        if user:
            raise ValidationError('این ایمیل قبلا وجود دارد')
        return user

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise ValidationError('این شماره تلفن قبلا وجود دارد')
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='ایمیل')
    password = forms.CharField(label= 'کلمه عبور', widget=forms.PasswordInput)








