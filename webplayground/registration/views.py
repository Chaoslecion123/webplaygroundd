from registration.forms import UserCreationFormWithEmail, ProfileForm , EmailForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from registration.models import Profile


class SingUpView(CreateView):
    # es un formuario generico
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    # con este metodo modificamos en tiempo de ejecucion el enlace 
    def get_success_url(self):
        return reverse_lazy('login') + '?register'
        # redireccionamos al login despues de hacer el registro
    # es un metedo para recuperar el formulario generico
    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        # modifica en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-class mb-2','placeholder':'nombre'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-class mb-2','placeholder':'email'})
        form.fields['password1'].widget = forms.TextInput(attrs={'class': 'form-class mb-2', 'placeholder': 'contraseña'})
        form.fields['password2'].widget = forms.TextInput(attrs={'class':'form-class mb-2','placeholder':'confirma contraseña'})
        return form


# este decorador sirve para que solamente puedan actualizar  el perfil los usuarios
# que esten autenticado
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):

        # recuperamos el objecto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperamos el objecto que se va a editar
        return self.request.user


    def get_form(self, form_class=None):
        # modifica en tiempo real
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget = forms.TextInput(attrs={'class': 'form-class mb-2', 'placeholder': 'Email'})
        return form



