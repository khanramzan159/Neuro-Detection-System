# Generated by Django 5.0.1 on 2024-03-16 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0014_user_status_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
