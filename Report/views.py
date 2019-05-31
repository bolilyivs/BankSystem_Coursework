from django.shortcuts import render
from .forms import *
from Structure.models import *
from CreditManager.tables import CreditTable
from DepositManager.tables import DepositTable
from PaymentManager.tables import PaymentTable

from django.http import HttpResponse
from django_xhtml2pdf.utils import generate_pdf, pdf_decorator
from django.db.models import Q

# Create your views here.
def FormReportView(request, title):
    form = ReportForm()
    return render(request, 'formReport.html', {'form': form, "title_form": title})

@pdf_decorator
def pdf(request, table, name = "Отчёт"):
    return render(request, 'reportPDF.html', {"table": table, "title_table": name})

def CreditFormReportView(request):
    title = "Отчёт: кредит"
    if request.method == 'POST':
        post = request.POST
        query = Credit.objects.filter(Q(reg_date__gte=post["reg_date_begin"]) & Q(reg_date__lte=post["reg_date_end"]))
        query = query.filter(Q(client__last_name__contains=post["client_last_name"]))
        query = query.filter(Q(client__first_name__contains=post["client_first_name"]))
        query = query.filter(Q(client__second_name__contains=post["client_second_name"]))

        table = CreditTable(query)
        return pdf(request, table, title)
    else:
        return FormReportView(request, title)

def DepositFormReportView(request):
    title = "Отчёт: Вклад"
    if request.method == 'POST':
        post = request.POST
        query = Deposit.objects.filter(Q(reg_date__gte=post["reg_date_begin"]) & Q(reg_date__lte=post["reg_date_end"]))
        query = query.filter(Q(client__last_name__contains=post["client_last_name"]))
        query = query.filter(Q(client__first_name__contains=post["client_first_name"]))
        query = query.filter(Q(client__second_name__contains=post["client_second_name"]))

        table = DepositTable(query)
        return pdf(request, table, title)
    else:
        return FormReportView(request, title)

def PaymentFormReportView(request):
    title = "Отчёт: Платежи"
    if request.method == 'POST':
        post = request.POST
        query = Payment.objects.filter(Q(reg_date__gte=post["reg_date_begin"]) & Q(reg_date__lte=post["reg_date_end"]))
        query = query.filter(Q(client__last_name__contains=post["client_last_name"]))
        query = query.filter(Q(client__first_name__contains=post["client_first_name"]))
        query = query.filter(Q(client__second_name__contains=post["client_second_name"]))

        table = PaymentTable(query)
        return pdf(request, table, title)
    else:
        return FormReportView(request, title)



