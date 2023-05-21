from django.db import models
# Create your models here.

class customers(models.Model):
    cust_id =models.AutoField(primary_key=True)
    cust_name=models.CharField(max_length=20)
    email_id =models.CharField(max_length=25)
    membership_status=models.CharField(max_length=10)
    pwd=models.CharField(max_length=10)
    class Meta:
        db_table='customers'


class books(models.Model):
    book_id =models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=45)
    genre =models.CharField(max_length=45)
    no_of_copies=models.IntegerField()
    class Meta:
        db_table='books'



class issued_books(models.Model):
    cust_name=models.CharField(max_length=20)
    book_name=models.CharField(max_length=45)
    copies_issued=models.IntegerField()
    class Meta:
        db_table='issued_books'
