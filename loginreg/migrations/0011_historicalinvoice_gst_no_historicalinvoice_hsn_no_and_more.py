# Generated by Django 5.0.1 on 2024-02-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0010_remove_historicalinvoice_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalinvoice',
            name='gst_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='historicalinvoice',
            name='hsn_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='gst_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='hsn_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
