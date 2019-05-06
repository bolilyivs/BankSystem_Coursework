from django.shortcuts import redirect
import django_tables2 as tables
from django_filters.views import FilterView
from django.views.generic.edit import *
from django.urls import reverse_lazy
from .tables import *
from .forms import *
from .filters import *
from Structure.models import * 
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta

client_succses_url = "/deposit/"

#############################
# All Operations
#############################

class DepositTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Deposit
    table_class = DepositTable
    queryset = Deposit.objects.all()
    template_name = "table.html"
    paginate_by = 20
    filterset_class = DepositFilter

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список вкладов"
        context['addbtn'] = "/deposit/"
        context['title_page'] = "Вклады"
        return context

class ReformedDepositTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Deposit
    table_class = DepositTable
    queryset = Deposit.objects.filter(end_date__lt = datetime.now())
    template_name = "tableView.html"
    paginate_by = 20
    filterset_class = DepositFilter

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список вкладов на переоформление"
        context['title_page'] = "Вклады"
        return context

#############################
# Deposti Tables
#############################

class ClientsDepositTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Client
    table_class = ClientsDepositTable
    queryset = Client.objects.all()
    template_name = "tableView.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Выбор клиентов"
        context['title_page'] = "Вклады"
        return context

class OneClientDepositTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Deposit
    table_class = DepositTable
    template_name = "table.html"
    paginate_by = 20
    filterset_class = DepositFilter

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список вкладов"
        context['addbtn'] = "add"
        context['title_page'] = "Вклады"
        return context
    
    def get(self, *args, **kwargs):
        self.clientpk = kwargs["clientpk"]
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Deposit.objects.filter(client=self.clientpk)

#############################
# Deposit Forms
#############################

class DepositCreateView(LoginRequiredMixin, CreateView):
    model = Deposit
    template_name = "form.html"
    form_class = DepositForm
    success_url = client_succses_url

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return client_succses_url + "{0}/".format(self.clientpk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Создать вклад"
        return context

    def post(self, request, *args, **kwargs):
        self.clientpk = kwargs["clientpk"]
        return super().post(request)
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.client = Client.objects.get(id=self.clientpk)
        instance.save() 
        return super().form_valid(form)

class DepositUpdateView(LoginRequiredMixin, UpdateView):
    model = Deposit
    template_name = "form.html"
    form_class = DepositForm

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    
    def get_success_url(self):
        return client_succses_url + "{0}/".format(self.clientpk)

    def post(self, request, *args, **kwargs):
        self.clientpk = kwargs["clientpk"]
        return super().post(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Редактирование вклада"
        return context

class DepositDeleteView(LoginRequiredMixin, DeleteView):
    model = Deposit
    template_name = "form_remove.html"
    form_class = DepositForm
    success_url = client_succses_url

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        self.clientpk = kwargs["clientpk"]
        return super().post(request)

    def get_success_url(self):
        return client_succses_url + "{0}/".format(self.clientpk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Удаление вклада"
        return context

#############################
# All Deposit Forms
#############################

class AllDepositUpdateView(LoginRequiredMixin, UpdateView):
    model = Deposit
    template_name = "form.html"
    form_class = DepositForm

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    
    def get_success_url(self):
        return client_succses_url + "all/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Редактирование кредита"
        return context

class AllDepositDeleteView(LoginRequiredMixin, DeleteView):
    model = Deposit
    template_name = "form_remove.html"
    form_class = DepositForm
    success_url = client_succses_url

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return client_succses_url + "all/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Удаление кредита"
        return context
