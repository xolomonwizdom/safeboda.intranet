# Generated by Django 3.0.6 on 2020-05-26 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickettype',
            name='category',
        ),
    ]