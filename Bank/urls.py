from django.contrib import admin
from django.urls import *
from ClientManager.views import *
from CreditManager.views import *
from DepositManager.views import *
from PaymentManager.views import *
from Structure.views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html")),
    path('profit/', ProfitView.as_view(), name="profit_view"),
    path('client/', ClientTableView.as_view(), name="client_view"),
    path('client/add/', ClientCreateView.as_view(), name="client_add"),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name="client_edit"),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name="client_delete"),

    path('credit/all/', CreditTableView.as_view(), name="credit_view_all"),
    path('credit/need/', NeedCreditTableView.as_view(), name="credit_view_need"),
    path('credit/bad/', NeedCreditTableView.as_view(), name="credit_view_bad"),
    path('credit/nonrepaid/', NonRepaidCreditTableView.as_view(), name="credit_view_nonrepaid"),
    path('credit/', ClientsCreditTableView.as_view(), name="credit_view"),
    path('credit/<int:clientpk>/', OneClientCreditTableView.as_view(), name="credit_client"),

    path('credit/<int:clientpk>/add', CreditCreateView.as_view(), name="credit_add"),
    path('credit/<int:clientpk>/edit/<int:pk>', CreditUpdateView.as_view(), name="credit_update"),
    path('credit/<int:clientpk>/delete/<int:pk>', CreditDeleteView.as_view(), name="credit_delete"),

    path('credit/all/edit/<int:pk>', AllCreditUpdateView.as_view(), name="credit_update_all"),
    path('credit/all/delete/<int:pk>', AllCreditDeleteView.as_view(), name="credit_delete_all"),
    
    path('deposit/all/', DepositTableView.as_view(), name="deposit_view_all"),
    path('deposit/reformed/', ReformedDepositTableView.as_view(), name="deposit_view_reformed"),
    path('deposit/', ClientsDepositTableView.as_view(), name="deposit_view"),
    path('deposit/<int:clientpk>/', OneClientDepositTableView.as_view(), name="deposit_client"),

    path('deposit/<int:clientpk>/add', DepositCreateView.as_view(), name="deposit_add"),
    path('deposit/<int:clientpk>/edit/<int:pk>', DepositUpdateView.as_view(), name="deposit_update"),
    path('deposit/<int:clientpk>/delete/<int:pk>', DepositDeleteView.as_view(), name="deposit_delete"),

    path('deposit/all/edit/<int:pk>', AllDepositUpdateView.as_view(), name="deposit_update_all"),
    path('deposit/all/delete/<int:pk>', AllDepositDeleteView.as_view(), name="deposit_delete_all"),

    path('payment/all/', PaymentTableView.as_view(), name="payment_view_all"),
    path('payment/', ClientsPaymentTableView.as_view(), name="payment_view"),
    path('payment/<int:clientpk>/', OneClientPaymentTableView.as_view(), name="payment_client"),

    path('payment/<int:clientpk>/add', PaymentCreateView.as_view(), name="payment_add"),
    path('payment/<int:clientpk>/edit/<int:pk>', PaymentUpdateView.as_view(), name="payment_update"),
    path('payment/<int:clientpk>/delete/<int:pk>', PaymentDeleteView.as_view(), name="payment_delete"),

    path('payment/all/edit/<int:pk>', AllPaymentUpdateView.as_view(), name="payment_update_all"),
    path('payment/all/delete/<int:pk>', AllPaymentDeleteView.as_view(), name="payment_delete_all"),
    
    path('accounts/login/', auth_views.LoginView.as_view(redirect_field_name="/"), {'next_page': '/'}, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(redirect_field_name="/"), name='logout' ),
]
APPEND_SLASH = True