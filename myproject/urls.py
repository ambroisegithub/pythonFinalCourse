"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp import views1
from myapp import views2
from myapp import viewsmenu
from myapp import viewstemplatsmodels
from myapp import viewsinheritance
# form_view2
urlpatterns = [
    path('home/',views.form_view),
    path('home1/',views1.form_view1),
    path('about/',views2.form_view2),
    path('admin/', admin.site.urls),
    path('menu/',viewsmenu.menu),
    path('viewstemplatsmodels/',viewstemplatsmodels.templates_view),
    path('base/',viewsinheritance.base,name='base'),
    path('page/',viewsinheritance.page,name='page'),
    path('index/',viewsinheritance.index,name='index'),
    
    
]

