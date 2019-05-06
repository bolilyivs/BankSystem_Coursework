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
from django.db.models import Q
from datetime import datetime, timedelta

client_succses_url = "/credit/"

#############################
# All Credit
#############################

class CreditTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Credit
    table_class = CreditTable
    queryset = Credit.objects.all()
    template_name = "table.html"
    paginate_by = 20
    filterset_class = CreditFilter

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список кредитов"
        context['addbtn'] = "/credit/"
        context['title_page'] = "Кредиты"
        return context

class NeedCreditTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Credit
    table_class = CreditTable
    queryset = Credit.objects.filter(active__exact=False,
     client__work__exact=True, client__conviction__exact=False, 
     client__house__gte = 100000, client__profit__gte=25000)
    template_name = "tableView.html"
    paginate_by = 20
    filterset_class = CreditFilter

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список кредитов на одобрение"
        context['title_page'] = "Кредиты"
        return context

class BadCreditTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Credit
    table_class = CreditTable
    queryset = Credit.objects.filter(Q(active__exact=False) & Q(client__work__exact=False) | Q(client__conviction__exact=True) | Q(client__house__lt = 100000))
    template_name = "tableView.html"
    paginate_by = 20
    filterset_class = CreditFilter

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список запрещённых кредитов"
        context['title_page'] = "Кредиты"
        return context

class NonRepaidCreditTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Credit
    table_class = CreditTable
    queryset = Credit.objects.filter(repaid__exact = False, end_date__lt = datetime.now())
    template_name = "tableView.html"
    paginate_by = 20
    filterset_class = CreditFilter

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список непогашенных кредитов"
        context['title_page'] = "Кредиты"
        return context

#############################
# Credit Tables
#############################

class ClientsCreditTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Client
    table_class = ClientsCreditTable
    queryset = Client.objects.all()
    template_name = "tableView.html"
    paginate_by = 20

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Выбор клиентов"
        context['title_page'] = "Кредиты"
        return context

class OneClientCreditTableView(LoginRequiredMixin, tables.SingleTableMixin, FilterView):
    model = Credit
    table_class = CreditTable
    template_name = "table.html"
    paginate_by = 20
    filterset_class = CreditFilter

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_table'] = "Список кредитов"
        context['addbtn'] = "add"
        context['title_page'] = "Кредиты"
        return context
    
    def get(self, *args, **kwargs):
        self.clientpk = kwargs["clientpk"]
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Credit.objects.filter(client=self.clientpk)

#############################
# Credit Forms
#############################

class CreditCreateView(LoginRequiredMixin, CreateView):
    model = Credit
    template_name = "form.html"
    form_class = CreditForm
    success_url = client_succses_url

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return client_succses_url + "{0}/".format(self.clientpk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Создать кредит"
        return context

    def post(self, request, *args, **kwargs):
        self.clientpk = kwargs["clientpk"]
        return super().post(request)
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.client = Client.objects.get(id=self.clientpk)
        instance.save() 
        return redirect(self.get_success_url())

class CreditUpdateView(LoginRequiredMixin, UpdateView):
    model = Credit
    template_name = "form.html"
    form_class = CreditForm

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    
    def get_success_url(self):
        return client_succses_url + "{0}/".format(self.clientpk)

    def post(self, request, *args, **kwargs):
        self.clientpk = kwargs["clientpk"]
        return super().post(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Редактирование кредита"
        return context

class CreditDeleteView(LoginRequiredMixin, DeleteView):
    model = Credit
    template_name = "form_remove.html"
    form_class = CreditForm
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
        context['title_form'] = "Удаление кредита"
        return context

#############################
# All Credit Forms
#############################

class AllCreditUpdateView(LoginRequiredMixin, UpdateView):
    model = Credit
    template_name = "form.html"
    form_class = CreditForm

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    
    def get_success_url(self):
        return client_succses_url + "all/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Редактирование кредита"
        return context

class AllCreditDeleteView(LoginRequiredMixin, DeleteView):
    model = Credit
    template_name = "form_remove.html"
    form_class = CreditForm
    success_url = client_succses_url

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return client_succses_url + "all/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_form'] = "Удаление кредита"
        return context
