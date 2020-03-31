from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import time
import re

d = {'name':'Abhrajeet Sarder'}
name = "Abhrajeet"
def HomeServer(request):
    return render(request,"home.html", {'name':name,                                   
    })
def add(request):
    try:
        num1 = int(request.POST['n1'])
        nnum2 = int(request.POST['n2'])
        sign = request.POST['sign']
        if(sign == "+"):
            add = num1+nnum2
        else:
            add = num1-nnum2
        return render(request, 'index.html', {'type':str(str(num1)+str(sign)+str(nnum2)+" = "),
                                          'rslt':str(add),
                                          'name':name,
                                          })
    except:
        return HttpResponse('<script>alert("Enter Valid Value");window.open("index.html","_self");</script>')
def enter(request):
    try:
        cal = str(request.POST['inputs'])
        m=cal.replace("X","*")
        d = m.replace("÷","/")
        if("." in cal):
            calc = float(eval(d))
        else:
            calc = eval(d)
            head, sep, tail = str(calc).partition(".")
            reg=re.compile('^[0]+$')
            regx = bool(reg.match(tail))
            if(regx == True):
                calc = int(eval(d))
            else:
                calc = eval(d)
        return render(request, 'home.html', {
            'result': str(str(cal)+" = "),
            'num': str(calc)
        })
    except Exception as e:
        print(e)
        return HttpResponse('<script>alert("Enter Valid Value");window.open("home.html","_self");</script>')
        #return HttpResponse(e)
def style(request):
    return render(request, "style.css")