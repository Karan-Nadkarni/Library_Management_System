# Generated by Django 3.0.7 on 2022-02-14 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib_man', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issued_books',
            name='copies_returned',
        ),
    ]
