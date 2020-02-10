from django.shortcuts import render
from django.views.generic.base import TemplateView

# Vistas basadas en clases
class HomePageView(TemplateView):
    template_name = "core/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = "Mi super Web Playgrounds"
    #     #context['latest_articles'] = Article.objects.all()[:5]
    #     return context
    
    # definimos la respuesta de la vista que funciona similar que en get_context_data
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Mi Super Web Playgrounds"})
    
class SamplePageView(TemplateView):
    template_name = "core/sample.html"

#====================================================================
# vistas basadas en funciones
# def sample(request):
#     return render(request, "core/sample.html")