from django.shortcuts import render
from django.http import HttpResponse
from myapp.form1 import LogForm
# Create your views here.

def form_view1(request):
    form1 = LogForm()
    if request.method == 'POST':
        form1 = LogForm(request.POST)
        if form1.is_valid():
            form1.save()    
    
    context = {"form":form1}
    return render(request,'home1.html',context)
    