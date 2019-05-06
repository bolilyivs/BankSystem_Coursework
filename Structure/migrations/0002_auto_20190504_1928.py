# Generated by Django 2.1.7 on 2019-05-04 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Structure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='house',
            field=models.DecimalField(decimal_places=2, default=120000, max_digits=20, verbose_name='Стоимость собственности'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='credit',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Одобрен'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='credit',
            name='repaid',
            field=models.BooleanField(default=False, verbose_name='Погашен'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deposittype',
            name='months',
            field=models.IntegerField(default=6, verbose_name='Месяцев'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='conviction',
            field=models.BooleanField(verbose_name='Судимость'),
        ),
        migrations.AlterField(
            model_name='client',
            name='profit',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Доход'),
        ),
        migrations.AlterField(
            model_name='client',
            name='work',
            field=models.BooleanField(verbose_name='Работа'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='credit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Structure.CreditType', verbose_name='Тип кредита'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='end_date',
            field=models.DateField(verbose_name='Конец срока'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='deposit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Structure.DepositType', verbose_name='Тип депозита'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='end_date',
            field=models.DateField(verbose_name='Конец срока'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='moneyoperation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Structure.Client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='moneyoperation',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Structure.Department', verbose_name='Отделение'),
        ),
        migrations.AlterField(
            model_name='moneyoperation',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Structure.Employee', verbose_name='Сотрудник'),
        ),
        migrations.AlterField(
            model_name='moneyoperation',
            name='money',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Деньги'),
        ),
        migrations.AlterField(
            model_name='moneyoperation',
            name='reg_date',
            field=models.DateField(verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='moneyoperation',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Structure.Status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='operationtype',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='operationtype',
            name='percent',
            field=models.FloatField(verbose_name='Процент'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='person',
            name='second_name',
            field=models.CharField(max_length=50, verbose_name='Отчество'),
        ),
    ]
