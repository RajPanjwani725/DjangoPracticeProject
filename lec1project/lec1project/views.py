from django.shortcuts import render,HttpResponse
from django.contrib import admin



def validation(request):
    return render(request,'validation.html')



def verify(request):
    if request.method == "POST":
        print("in verify-----------------")
        name = request.POST.get('username')
        pword = request.POST.get('pword')
# and pword=='27966@Raj@725'
        if(name=='725@Raj@27966'and pword=='27966@Raj@725'):
            return render(request, 'validation.html', {'k1': 'admin'})
        else:
            return render(request,'validation.html',{'k2':'Wrong Email Address or password  '})
