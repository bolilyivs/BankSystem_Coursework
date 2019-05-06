from Structure.models import *
import django_tables2 as tables

#############################
# Client
#############################

class ClientTable(tables.Table):
    edit = tables.TemplateColumn('<a href="edit/{{record.pk}}">{% load icons %} {% icon "pencil" %} </a>',verbose_name=' ',)
    delete = tables.TemplateColumn('<a href="delete/{{record.pk}}/">{% load icons %} {% icon "trash" %} ',verbose_name=' ',)

    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'second_name', 'profit', 'conviction', 'work', 'house','edit', 'delete']