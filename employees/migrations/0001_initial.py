# Generated by Django 4.1.1 on 2022-09-24 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('surname', models.CharField(max_length=127)),
                ('login', models.CharField(max_length=127)),
                ('password', models.CharField(max_length=1023)),
                ('email', models.EmailField(max_length=254)),
                ('employee_role', models.CharField(choices=[('Default', 'Default'), ('PM', 'Pm'), ('Administrator', 'Administrator')], max_length=31)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_login_date', models.DateField(auto_now=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.department')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('project_status', models.CharField(choices=[('Planned', 'Planned'), ('Ongoing', 'Ongoing'), ('Stopped', 'Stopped')], max_length=31)),
                ('created_status', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('stop_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeInProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee')),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.project')),
            ],
        ),
    ]