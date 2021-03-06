# Generated by Django 4.0.3 on 2022-04-01 13:52

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
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_email', models.CharField(max_length=200, null=True)),
                ('company_walletId', models.CharField(blank=True, max_length=100)),
                ('company_avatars', models.ImageField(blank=True, null=True, upload_to='company_avatars/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('companyuser', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_email', models.CharField(max_length=200, null=True)),
                ('personal_walletId', models.CharField(blank=True, max_length=100)),
                ('avatars', models.ImageField(blank=True, default='imgs/avatar.jpg', null=True, upload_to='avatars/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customeruser', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Performance', 'Performance'), ('exhibition', 'exhibition')], max_length=200, null=True)),
                ('eventname', models.CharField(max_length=200, null=True)),
                ('eventdescription', models.CharField(blank=True, max_length=200, null=True)),
                ('eventticketnumber', models.IntegerField()),
                ('eventprice', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('totalorderedTicket', models.IntegerField(default=0)),
                ('remainedTicketNum', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_StartTime', models.DateTimeField(null=True)),
                ('date_EndTime', models.DateTimeField(null=True)),
                ('event_pic', models.ImageField(blank=True, null=True, upload_to='C:\\DjangoEnv\\NFTTicketPlatform\\media')),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('Ongoing', 'Ongoing'), ('Expired', 'Expired')], default='Not Started', max_length=200, null=True)),
                ('companycreater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='authentication.companyprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNumber', models.IntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('orderTotalPrice', models.DecimalField(decimal_places=4, max_digits=5)),
                ('status', models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], max_length=200, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.customerprofile')),
                ('events', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.events')),
            ],
        ),
    ]
