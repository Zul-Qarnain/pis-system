from django.shortcuts import render

def Admin(request):
    return render(request,'admin.html')
def Invalid(request):
    return render(request,'invalid.html')
def AddAccount(request):
    return render(request,'addaccount.html')

def MyProfile(request):
    return render(request,'myprofile.html')

def ViewProfile(request):
    return render(request,'viewstudent.html')

def AddStudent(request):
    return render(request, 'addstudent.html')

def Main(request):
    return render(request, 'main.html')
