from django.forms import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from Structure.models import *

class ReportForm(Form):

    reg_date_begin = DateField(label='Дата от', widget = DateInput(attrs={'type':'date'}), required=True)
    reg_date_end = DateField(label='Дата от', widget = DateInput(attrs={'type':'date'}), required=True)

    client_last_name = CharField(label='Фамилия клиента', max_length=100, required=False)
    client_first_name = CharField(label='Имя клиента', max_length=100, required=False)
    client_second_name = CharField(label='Отчество клиента', max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Запрос'))
        
