# Generated by Django 4.0.3 on 2022-04-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('transferring', 'transferring'), ('UnConfirmed', 'UnConfirmed'), ('Valid', 'Valid'), ('Used', 'Used')], default='UnConfirmed', max_length=200, null=True),
        ),
    ]