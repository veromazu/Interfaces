from django import forms
from django.contrib.auth.forms import UserCreationForm 
from interfaz.models import *
from django.contrib.auth import authenticate

class RegisterForm(UserCreationForm):

    CHOICES = (
        ('Estudiante', 'Estudiante'),
        ('Profesor', 'Profesor'),
        ('Representante','Representante'),
        ('Médico','Médico'),
        ('Investigador','Investigador'),
    )

    class Meta:
        model = User
        fields = ('email','first_name','last_name','password1','password2')
    
    rol = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            #self.fields[key].widget.attrs['class'] = 'form-control'
            self.fields[key].widget.attrs['required'] = True
            self.fields[key].widget.attrs['id'] = 'id_'+key
            #self.fields[key].widget.attrs['placeholder'] = self.fields[key].label

    def clean_email(self):
        email = self.cleaned_data.get('email')   
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con ese email.")
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'required':'True'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'type':'password','required':'True'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    
    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if user is None:
            raise forms.ValidationError("Los datos son invalidos.")
        return password