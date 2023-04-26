from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView
from .utils import DataMixin
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import TemplateView

class Home(DataMixin, TemplateView):
    #model =
    template_name = 'mainapp/home.html'
    #context_object_name = 'posts'
    #extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['menu'] = menu
        #context['title'] = 'Главная страница'
        #context['cat_selected'] = 0
        c_def = self.get_user_context(title="Главная страница", home_selected=True)
        return dict(list(context.items()) + list(c_def.items()))
