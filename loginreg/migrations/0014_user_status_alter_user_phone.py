# Generated by Django 5.0.1 on 2024-03-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0013_delete_admin_remove_historicalitem_history_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
