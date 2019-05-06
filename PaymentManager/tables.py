from Structure.models import *
import django_tables2 as tables

#############################
# Client Operations
#############################
# Payment
#############################

class ClientsPaymentTable(tables.Table):
    add = tables.TemplateColumn('<a href="{{record.pk}}">{% load icons %} {% icon "plus-circle" %} </a>',verbose_name=' ',)
    
    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'second_name', 'profit', 'conviction', 'work', 'add']

#############################
# All Operations
#############################

class PaymentTable(tables.Table):
    edit = tables.TemplateColumn('<a href="edit/{{record.pk}}">{% load icons %} {% icon "pencil" %} </a>',verbose_name=' ',)
    delete = tables.TemplateColumn('<a href="delete/{{record.pk}}">{% load icons %} {% icon "trash" %} ',verbose_name=' ',)
    class Meta:
        model = Payment    
        fields = ['client', 'money', 'status', 'department', 'employee', 'reg_date', 'edit', 'delete']