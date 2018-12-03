from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from messenger.models import Thread, Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
# Create your views here.

@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    model = Thread
    template_name = 'messenger/thread_list.html'
    """
    #filtramos un queryset por defecto
    def get_queryset(self):
        # recuperamos el mismo queryset llamando a la superclase
        queryset = super(ThreadList).get_queryset()
        return queryset.filter(users=self.request.user) # asi filtrariamos por el usuario que esta identificado en este momento
        
        necesitamos estar seguros de que algun usuario a iniciado la sesion para ello nos apoyamos de los decoradores
        """

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread


    def get_object(self, queryset=None):  #recuperamos el objecto detail
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

def add_message(request, pk):
    json_response = {'created': False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            if len(thread.messages.all()) is 1:
                json_response['first'] = True


    else:
        raise Http404('User is not authenticaded')

    return JsonResponse(json_response)

@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args= [thread.pk]))

