# Generated by Django 4.0.3 on 2022-04-04 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='status',
            field=models.CharField(choices=[('UnConfirmed', 'UnConfirmed'), ('Confirmed', 'Confirmed'), ('Success', 'Success')], default='UnConfirmed', max_length=200, null=True),
        ),
    ]
