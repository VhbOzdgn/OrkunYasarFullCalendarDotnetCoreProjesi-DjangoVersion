from django import forms
from .models import AppUser

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label="Kullanıcı Adı", required=True)
    first_name = forms.CharField(max_length=30, label="Adı", required=True)
    last_name = forms.CharField(max_length=30, label="Soyadı", required=True)
    password1 = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, label="Parola Doğrulama", widget=forms.PasswordInput)
    color = forms.CharField(label="Renk",widget=forms.TextInput(attrs={'type': 'color'}))
    
    class Meta:
        model = AppUser
        fields =(
            'username',
            'first_name',
            'last_name',
            'color',
            'role',
            'email',
            'password1',
            'password2',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parola alanları uyuşmuyor')
        return password2
    


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Kullanıcı Adı")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Beni Hatırla",required=False)