from django import forms
from django.contrib.auth.password_validation import validate_password

class ContactForm(forms.Form):
    
    name=forms.CharField(max_length=100, label="Nombre")
    email=forms.CharField(label="Email")
    message=forms.CharField(max_length=500, label="Mensaje", widget=forms.Textarea)

    def clean_name(self):
        name=self.cleaned_data.get('name')
        if len(name)<5:
            raise forms.ValidationError("El nombre debe tener almenos 5 caracteres")
        return name
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError("El formato del email no es correcto")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(max_length=140, label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")


class UserRegisterForm(forms.Form):
    username= forms.CharField(max_length=140, label="Nombre de usuario")
    first_name=forms.CharField( max_length=140, label="Nombre")
    last_name=forms.CharField(max_length=140, label="Apellidos")
    email=forms.CharField(max_length=140, label="Email")

    password1=forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2=forms.CharField(widget=forms.PasswordInput, label="Repite Contraseña")

    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")

        if password1 != password2 and password1 != '':
            raise forms.ValidationError('Las contraseñas no coinciden')
        
        if password2 != '':
            validate_password(password2)
        
        return password2
    
            
