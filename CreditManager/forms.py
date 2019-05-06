from django.forms import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from Structure.models import *


class CreditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Сохранить'))

    class Meta:
        model = Credit
        fields = '__all__'
        exclude = ('client',)

        widgets = {
            'reg_date': DateInput(attrs={'type':'date'}),
            'end_date': DateInput(attrs={'type':'date'}),
        }


    

    

        