# Generated by Django 5.0.1 on 2024-02-11 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0006_historicalinvoice_historicalitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinvoice',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
