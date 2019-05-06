from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)

class Person(models.Model):
    first_name  = models.CharField(max_length=50, verbose_name="Имя")
    second_name  = models.CharField(max_length=50, verbose_name="Отчество")
    last_name  = models.CharField(max_length=50, verbose_name="Фамилия")

    def __str__(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.second_name,)

class Client(Person):
    conviction = models.BooleanField(verbose_name="Судимость")
    work = models.BooleanField(verbose_name="Работа")
    house = models.DecimalField(max_digits=20, decimal_places=2,verbose_name="Стоимость собственности") ############
    profit = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Доход")

class Employee(Person):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, verbose_name="Пользователь")
    pass

class OperationType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    percent = models.FloatField(verbose_name="Процент")

    def __str__(self):
        return "{}, {}%".format(self.name, self.percent)

class CreditType(OperationType):
    pass

class DepositType(OperationType):
    months = models.IntegerField(verbose_name="Месяцев") ############
    
    def __str__(self):
        return "{}, {}%, {} мес.".format(self.name, self.percent, self.months)

class MoneyOperation(models.Model):
    money = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Деньги")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Отделение")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус")
    reg_date = models.DateField(verbose_name="Дата регистрации")

    def __str__(self):
        return "Операция: {}, {}".format(self.money, self.client)

class Credit(MoneyOperation):
    credit_type = models.ForeignKey(CreditType, on_delete=models.CASCADE, verbose_name="Тип кредита")
    end_date = models.DateField(verbose_name="Конец срока")
    active = models.BooleanField(verbose_name="Одобрен") ############
    repaid = models.BooleanField(verbose_name="Погашен") ############

class Deposit(MoneyOperation):
    deposit_type = models.ForeignKey(DepositType, on_delete=models.CASCADE, verbose_name="Тип депозита")
    end_date = models.DateField(verbose_name="Конец срока")

class Payment(MoneyOperation):
    pass
