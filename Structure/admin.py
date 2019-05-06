from django.contrib import admin
from Structure.models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Employee)

admin.site.register(Credit)
admin.site.register(Deposit)
admin.site.register(Payment)

admin.site.register(CreditType)
admin.site.register(DepositType)

admin.site.register(Department)
admin.site.register(Status)
