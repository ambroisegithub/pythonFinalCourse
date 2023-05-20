from django.shortcuts import render
from django.http import HttpResponse
from .modelstemplates import MenuTemplates
def templates_view(request):
    newmenu = MenuTemplates.objects.all()
    menu_dict ={'menu1':newmenu}
    return render(request, 'templatemodel.html',menu_dict)