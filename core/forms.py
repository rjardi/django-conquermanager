from django import forms

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

            
