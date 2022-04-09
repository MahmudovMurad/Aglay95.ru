from multiprocessing import context, get_context
from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView

from store.models import Product

from .models import *
from rest_framework.generics import CreateAPIView
from rest_framework import serializers

class HomePage(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.all()[:2]
        context['banner'] = Banner.objects.all()
        context['reklam'] = Product.objects.all()[:3]
        return context

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
            )



class SubscribeAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer


class BlogList(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_list'] = Blog.objects.all()
        return context