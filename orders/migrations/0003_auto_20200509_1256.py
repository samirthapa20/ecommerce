# Generated by Django 3.0.5 on 2020-05-09 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200509_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='active',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billing_profile',
        ),
    ]
