from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    
    menus ={
        'mains':[
       {"name":"muhayimana ambroise","age":"20"},
       {"name":"shakur pak","age":"30"},
       {"name":"khalifa wiz","age":"27"},
       {"name":"john drille","age":"29"},
        ]
    }
    

    
    return render(request,'menu.html',menus)
    