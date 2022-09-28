# Generated by Django 4.1.1 on 2022-09-26 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_options_alter_employee_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='last_login_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(max_length=127, null=True),
        ),
    ]
