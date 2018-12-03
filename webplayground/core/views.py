from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):

    template_name = 'core/home.html'

    # este get es la respuesta de la vista
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'title':'Ciencia de Datos','title2':'Pilares de Informacion'})


    #sobreescribimos el diccionario de contexto
    # def get_context_data(self,**kwargs):
    	#  context = super().get_context_data(**kwargs)
    	# context['lest_articles'] = Article.objecets.all()[:5]
    	# return context 

class SamplePageView(TemplateView):

    template_name = 'core/sample.html'