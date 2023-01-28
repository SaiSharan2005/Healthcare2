# Generated by Django 4.1.5 on 2023-01-28 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Profile_pic', models.ImageField(default='doctor.png', null=True, upload_to='')),
                ('Date_of_birth', models.DateField(null=True)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('Experience', models.PositiveIntegerField()),
                ('Position', models.CharField(max_length=30)),
                ('Profession', models.CharField(max_length=100)),
                ('About_me', models.TextField(max_length=500)),
                ('Education_from', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField(blank=True)),
                ('host', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medical_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='None ', max_length=300)),
                ('Report_name', models.CharField(max_length=100)),
                ('Hospital', models.CharField(max_length=100)),
                ('Patient_name', models.CharField(max_length=100)),
                ('Doctor_name', models.CharField(max_length=100)),
                ('Date_of_scan', models.DateTimeField()),
                ('Date_of_recieved', models.DateTimeField()),
                ('doctor_prescription', models.TextField(default='None ', max_length=300)),
                ('Blood_pressure', models.IntegerField()),
                ('Sugar_level', models.IntegerField()),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(default='avater.svg', null=True, upload_to='')),
                ('Date_of_birth', models.DateField(null=True)),
                ('user_relationship', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room_doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_to_doc', models.CharField(max_length=300)),
                ('message_to_pat', models.CharField(max_length=500, null=True)),
                ('Doctor_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Health.doctor')),
                ('Patient_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Health.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Remainder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Remainder_date', models.DateField()),
                ('Remainder_time', models.TimeField()),
                ('Remainder_message', models.CharField(max_length=100)),
                ('coice', models.BooleanField(default=False, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_tablets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=100, null=True)),
                ('parameters_value', models.CharField(max_length=100, null=True)),
                ('parameter_date_time', models.DateTimeField()),
                ('Extra_parameters', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Health.medical_report')),
            ],
        ),
        migrations.AddField(
            model_name='medical_report',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Health.patient'),
        ),
        migrations.CreateModel(
            name='Extra_Values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=100)),
                ('parameters_value', models.CharField(max_length=100)),
                ('Extra_parameters', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Health.medical_report')),
            ],
        ),
    ]