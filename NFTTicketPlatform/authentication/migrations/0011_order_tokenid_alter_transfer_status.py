# Generated by Django 4.0.3 on 2022-04-04 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_transfer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tokenID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='status',
            field=models.CharField(choices=[('Sent', 'Sent'), ('UnConfirmed', 'UnConfirmed'), ('Confirmed', 'Confirmed'), ('Success', 'Success')], default='UnConfirmed', max_length=200, null=True),
        ),
    ]