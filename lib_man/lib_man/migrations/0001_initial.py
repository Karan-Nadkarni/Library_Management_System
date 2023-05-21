# Generated by Django 3.0.7 on 2022-02-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=45)),
                ('genre', models.CharField(max_length=45)),
                ('no_of_copies', models.IntegerField()),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='customers',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=25)),
                ('membership_status', models.CharField(max_length=10)),
                ('pwd', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='issued_books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=20)),
                ('book_name', models.CharField(max_length=45)),
                ('copies_issued', models.IntegerField()),
                ('copies_returned', models.IntegerField()),
            ],
            options={
                'db_table': 'issued_books',
            },
        ),
    ]
