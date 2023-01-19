from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse
class cbv_page(TemplateView):
    template_name='cbv_page.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='ASHU'
        context['age']=3
        return context
    
class cbv_form(TemplateView):
    template_name='cbv_form.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=StudentForm()
        return context
    
    def post(self,request):
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))




    











