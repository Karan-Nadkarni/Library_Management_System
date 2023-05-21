from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .model import customers
from .model import books
from .model import issued_books

# Create your views here.

def home(request):
    return render(request, 'HTML/homepage.html')

def bi(request):
    return render(request, 'HTML/bookissue.html')

def br(request):
    return render(request, 'HTML/bookreturn.html')

def sr(request):
    return render(request, 'HTML/membership_renew.html')

def reg(request):
    return render(request, 'HTML/register.html')

def signin(request):
    return render(request, 'HTML/signin.html')

def signout(request):
    return render(request, 'HTML/signout.html')

def regsub(request):
    en=customers(cust_name=request.POST.get('name'),email_id=request.POST.get('email'),pwd=request.POST.get('pwd'),membership_status="Created")
    en.save()
    print("Congratulations , you are now a member !!!")
    return render(request,'HTML/register.html')

def login_sub(request):
    obj1 = customers.objects.get(cust_name=request.POST.get('name'))
    obj1.membership_status = "online"
    obj1.save()
    print("You have been logged in successfully")
    return render(request,'HTML/signin.html')

def logout_sub(request):
    obj1 = customers.objects.get(cust_name=request.POST.get('name'))
    obj1.membership_status = "offline"
    obj1.save()
    print("You have been logged out successfully")
    return render(request,'HTML/signout.html')

def bi_sub(request):

    en=issued_books(cust_name=request.POST.get('name'),book_name=request.POST.get('book'),copies_issued=request.POST.get('copies'))
    en.save()

    obj1=books.objects.get(book_name=request.POST.get('book'))
    print(obj1)
    nop=int(obj1.no_of_copies)
    if(nop<=0):
        print("Selected book is not available , Sorry")
        return render(request,'HTML/bookissue.html')
    else:
        i_copies=request.POST.get('copies')
        nc=int(i_copies)
        nop=nop-nc
        nop=str(nop)
        obj1.no_of_copies=nop
        obj1.save()
        print("Book issued successfully")
        return render(request,'HTML/bookissue.html')


def br_sub(request):

    obj1=books.objects.get(book_name=request.POST.get('book'))
    nop=int(obj1.no_of_copies)
    if(nop>=5):
        print("All issued copies of this book have been returned")
        return render(request,'HTML/bookreturn.html')
    else:
        i_copies=request.POST.get('copies')
        nc=int(i_copies)
        nop=nop+nc
        nop=str(nop)
        obj1.no_of_copies=nop
        obj1.save()
        print("Book returned successfully")
        return render(request,'HTML/bookreturn.html')
