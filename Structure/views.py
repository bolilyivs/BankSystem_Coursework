from django.shortcuts import render
import django_tables2 as tables
from django.views.generic.edit import *
from django.urls import reverse_lazy
from Structure.models import * 
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms


class ProfitFilter(forms.Form):
    reg_date__gt = forms.DateField(label = "Дата с:", required=False, widget=forms.DateInput(attrs={'type':'date'}))
    reg_date__lt = forms.DateField(label = "до:", required=False, widget=forms.DateInput(attrs={'type':'date'}))


class ProfitTable(tables.Table):
    profit = tables.Column(verbose_name= "Деньги")
    reg_date = tables.Column(verbose_name= "Дата")

class ProfitView(LoginRequiredMixin, FormMixin, tables.SingleTableView):
    form_class = ProfitFilter
    table_class = ProfitTable
    template_name = "table_time.html"
    paginate_by = 10
    filterset_class = ProfitFilter

    def getMoney(self, objs):
        money = 0
        for obj in objs:
            money += float(obj.money)
        return money  

    def get(self, request, *args, **kwargs):
        self.reg_date_gt = ""
        self.reg_date_lt = ""
        
        if request.GET.get('reg_date__gt'):
            self.reg_date_gt = request.GET["reg_date__gt"]
        if request.GET.get('reg_date__gt'):
            self.reg_date_lt = request.GET["reg_date__lt"]
        return super().get( request, *args, **kwargs)

    def get_queryset(self):   
        start_date = datetime.now()
        if self.reg_date_gt != "":
            start_date = datetime.strptime(self.reg_date_gt, "%Y-%m-%d")

        end_date = datetime.now()
        if self.reg_date_lt != "":
            end_date = datetime.strptime(self.reg_date_lt, "%Y-%m-%d")
        
        data = []

        for i in range( (end_date-start_date).days ) :
            credits = Credit.objects.filter(reg_date__exact= (start_date + timedelta(days=i)))
            deposits = Deposit.objects.filter(reg_date__exact= (start_date + timedelta(days=i)))
            payments = Payment.objects.filter(reg_date__exact= (start_date + timedelta(days=i)))
            
            money = self.getMoney(deposits) + self.getMoney(payments) - self.getMoney(credits)

            data.append({"profit": str(money), "reg_date": str(start_date + timedelta(days=i))})

        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Финансы"
        context['title_table'] = "Доходы"
        print(context)
        return context
            

