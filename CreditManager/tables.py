from Structure.models import *
import django_tables2 as tables

# Credits
#############################

class ClientsCreditTable(tables.Table):
    add = tables.TemplateColumn('<a href="{{record.pk}}">{% load icons %} {% icon "plus-circle" %} </a>',verbose_name=' ',)

    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'second_name', 'profit', 'conviction', 'work', 'add']

#############################
# All Operations
#############################

class CreditTable(tables.Table):
    edit = tables.TemplateColumn('<a href="/credit/all/edit/{{record.pk}}">{% load icons %} {% icon "pencil" %} </a>',verbose_name=' ',)
    delete = tables.TemplateColumn('<a href="/credit/all/delete/{{record.pk}}">{% load icons %} {% icon "trash" %} ',verbose_name=' ',)
    class Meta:
        model = Credit
        fields = ['client', 'money', 'status', 'department', 'employee', 'credit_type', 'reg_date', 'end_date', 'active', 'repaid', 'edit', 'delete']