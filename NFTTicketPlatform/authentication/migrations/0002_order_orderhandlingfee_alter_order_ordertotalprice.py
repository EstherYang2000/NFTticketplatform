# Generated by Django 4.0.3 on 2022-04-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderHandlingfee',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderTotalPrice',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=5),
        ),
    ]
