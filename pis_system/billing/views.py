from django.http import HttpResponseRedirect
from django.shortcuts import render
from pis_system.forms import *
from pis_system.models import *

def billing(request):
    
    students = STUDENT.objects.order_by('stud_id')
    userid = request.POST.get('userID')
    passwords = request.POST.get('password')
    if request.session.get('is_logged_in', False):
        user = {'name': request.session['name'], 'id': request.session['userID']}
        item_search = ItemSearch()
        return render(
                        request, 
                        './billing/home.html', 
                        {
                            'system_name': 'Enrolment System', 
                            'user': user, 
                            'students': students,
                            'item_search': item_search
                        }
                      )
    
    if request.method == 'POST':
        
        try:
            username = EMPLOYEE.objects.get(emp_id = userid)
        except EMPLOYEE.DoesNotExist:
            username = None
        
        if username is None:
            form=LogInForm()
            return render(
                            request, 
                            'login.html', 
                            {
                                'form': form, 
                                'system_name': 'Billing System',
                                'cover_url':'static/images/billing_cover.jpg'
                            }
                          )

        else:
            if username.password == passwords:
                request.session['is_logged_in'] = True
                request.session['userID'] = username.emp_id
                request.session['password'] = username.password
                request.session['name'] = username.firstname+' '+username.mi+' '+username.lastname
                user = {'name': request.session['name'], 'id': request.session['userID']}
                item_search = ItemSearch()
                return render(
                                request, 
                                './billing/home.html', 
                                {
                                    'system_name': 'Enrolment System', 
                                    'user': user, 
                                    'students': students,
                                    'item_search': item_search
                                }
                              )
    else:
            form=LogInForm()
            return render(
                            request, 
                            'login.html', 
                            {
                                'form': form, 'system_name': 'Billing System', 
                                'cover_url': 'static/images/billing_cover.jpg'
                            }
                          )
