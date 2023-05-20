from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def form_view2(request):
    context = {"text":'Learn how to create a basic Django template using best-practice principles to ensure an efficient and maintainable build.Learn how to create a basic Django template using best-practice principles to ensure an efficient and maintainable build.Learn how to create a basic Django template using best-practice principles to ensure an efficient and maintainable build.'}
    return render(request,'about.html',context)

# templates in django
    