from django.shortcuts import render
import django_tables2 as tables
from django_filters.views import FilterView
from django.views.generic.edit import *
from django.urls import reverse_lazy
from .tables import *
from .forms import *
from Structure.models import * 
from django.contrib.auth.mixins import LoginRequiredMixin

#############################
# Client Table
#############################

class ClientTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Client
    table_class = ClientTable
    queryset = Client.objects.all()
    template_name = "table.html"
    paginate_by = 20

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список клиентов"
        context['addbtn'] = "add"
        context['title_page'] = "Клиенты"
        return context

#############################
# Client Forms
#############################

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = "form.html"
    form_class = ClientForm
    success_url = '/client/'

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Добавить клиента"
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = "form.html"
    form_class = ClientForm
    success_url = '/client/'

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Редактирование клиента"
        return context

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = "form_remove.html"
    form_class = ClientForm
    success_url = '/client/'

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Удаление клиента"
        return context