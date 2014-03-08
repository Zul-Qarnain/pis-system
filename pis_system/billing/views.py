from django.http import HttpResponseRedirect
from django.shortcuts import render
from pis_system.forms import *
from pis_system.models import *
userid=''

def billing(request):
    #LOGGED_IN=False
    #userid=request.POST.get('userID')
    #passwords=request.POST.get('password')
    username=EMPLOYEE.objects.get(emp_id=userid)

    name=username.firstname+' '+username.mi+' '+username.lastname
    userID=username.emp_id
    user = {'name':name, 'id':userID}
    item_search = ItemSearch()
    return render(request, './billing/home.html', {'system_name':'Enrolment System', 'user':user, 'item_search':item_search})


def login(request):
    form=LogInForm()
    return render(request, 'login.html', {'form':form, 'system_name':'Billing System', 'cover_url':'static/images/billing_cover.jpg'})

def login_auth(request):
    global userid
    userid=request.POST.get('userID')
    passwords=request.POST.get('password')
    username=EMPLOYEE.objects.get(emp_id=userid)

    if username.password==passwords:
        if username.position=='Faculty':
            return HttpResponseRedirect('billing')
    else:
        return HttpResponseRedirect('login')

