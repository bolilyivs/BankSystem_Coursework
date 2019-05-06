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

client_succses_url = "/payment/"

#############################
# All Operations
#############################

class PaymentTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Payment
    table_class = PaymentTable
    queryset = Payment.objects.all()
    template_name = "table.html"
    paginate_by = 20
    filterset_class = PaymentFilter

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список платежей"
        context['addbtn'] = "/payment/"
        context['title_page'] = "Платежи"
        return context


#############################
# Deposti Tables
#############################

class ClientsPaymentTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Client
    table_class = ClientsPaymentTable
    queryset = Client.objects.all()
    template_name = "tableView.html"
    paginate_by = 20

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Выбор клиентов"
        context['title_page'] = "Платежи"
        return context

class OneClientPaymentTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Payment
    table_class = PaymentTable
    template_name = "table.html"
    paginate_by = 20
    filterset_class = PaymentFilter

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список платежей"
        context['addbtn'] = "add"
        context['title_page'] = "Платежи"
        return context
    
    def get(self, *args, **kwargs):
        self.clientpk = kwargs["clientpk"]
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Payment.objects.filter(client=self.clientpk)

#############################
# Payment Forms
#############################

class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    template_name = "form.html"
    form_class = PaymentForm
    success_url = client_succses_url

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return client_succses_url + "{0}/".format(self.clientpk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Создать платеж"
        return context

    def post(self, request, *args, **kwargs):
        self.clientpk = kwargs["clientpk"]
        return super().post(request)
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.client = Client.objects.get(id=self.clientpk)
        instance.save() 
        return super().form_valid(form)

class PaymentUpdateView(LoginRequiredMixin, UpdateView):
    model = Payment
    template_name = "form.html"
    form_class = PaymentForm

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    
    def get_success_url(self):
        return client_succses_url + "{0}/".format(self.clientpk)

    def post(self, request, *args, **kwargs):
        self.clientpk = kwargs["clientpk"]
        return super().post(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Редактирование платежа"
        return context

class PaymentDeleteView(LoginRequiredMixin, DeleteView):
    model = Payment
    template_name = "form_remove.html"
    form_class = PaymentForm
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
        context['title_form'] = "Удаление платежа"
        return context


#############################
# All Payment Forms
#############################

class AllPaymentUpdateView(LoginRequiredMixin, UpdateView):
    model = Payment
    template_name = "form.html"
    form_class = PaymentForm

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    
    def get_success_url(self):
        return client_succses_url + "all/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Редактирование кредита"
        return context

class AllPaymentDeleteView(LoginRequiredMixin, DeleteView):
    model = Payment
    template_name = "form_remove.html"
    form_class = PaymentForm
    success_url = client_succses_url

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return client_succses_url + "all/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Удаление кредита"
        return context
