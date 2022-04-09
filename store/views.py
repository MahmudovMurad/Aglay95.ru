from django.shortcuts import render
from django.views.generic.base import TemplateView
from store.models import Product
from django.views.generic import ListView, DetailView, CreateView
from .form import *
from .models import *

class ProductList(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Product.objects.all()[:6] 
        context['premium'] = Product.objects.all()[:3]
        return context

def product_detail(request, id):
    post = Product.objects.get(id=id)
    
    context = {
        "post" : post
    }
    
    return render(request, "detail.html", context)



class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    print("Contact")
    def get_success_url(self):
        return reverse_lazy('store:store')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context