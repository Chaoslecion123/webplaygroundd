from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from pages.forms import PagesForm
# from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


# un mixin es una implementacio de funcionalidades para una clase podemos
#implementarlas en cualquier lugar dandole prioridad a la funcion que a la misma clase
# object es la clase base de todas las clases de python
# este mixin requerira que el usuario sea miembro del staf
class StaffRequiredMixin(object):
    # con el dispatch te permite recuperar la misma peticion si es anonymoUser o si es un 
    # usuario .
    # este decorador te permite saber si eres miembre del staf y ahorrar codigo
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.is_staff:
        #   return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.
class PagesListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page
    
@method_decorator(staff_member_required,name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PagesForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PagesForm
    template_name_suffix = '_update_form'
    # recuperar el indentificador con el objecto que se esta editando que te
    # permite recuperar la respuesta
    # con el dispatch te permite recuperar la misma peticion
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')

class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

