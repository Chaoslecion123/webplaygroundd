from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from registration.models import Profile

# extender el formulario de usercreationform generico
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como minimo y debe ser valido')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # extender email si es posible por que ya pertenece al formulario generico
        # solo lo estamos activando

    # esto es una validacion para email y debe comenzar como clean_
    def clean_email(self):
        email = self.cleaned_data.get("email")  #obtienes el valor del campo email del formulario
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya esta registrado, prueba con otro')
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografia'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como minimo y debe ser valido')

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")  # obtienes el valor del campo email del formulario
        if 'email' in self.cleaned_data: # es una lista que almacena todos los campos que se han editado en el formulario
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya esta registrado, prueba con otro')
        return email

