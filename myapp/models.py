from django.db import models
from unicodedata import name
# Create your models here.
class Menu(models.Model):
    fName = models.CharField(max_length = 80)
    lName = models.CharField(max_length = 80)
    email = models.EmailField(max_length = 70)
    age = models.IntegerField()
    
    def __str__(self):
            return self.fName + ' : ' + self.lName + ' : ' + self.email  
        


class reservations(models.Model):
    
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    booking_time = models.DateTimeField(auto_now_add=True)        
          
# comands to create,get,etc

# type command "python3 manage.py shell" to access shell
# "Menu.objects.all()" to get all
# to create
# A = Menu.objects.create(firstName = "John", lastName = "doe",email= "john@example.com",age= 25)
# you can update models like to change lastName into lName
# Also yo can run the command called "python3 manage.py makemigrations"
# python3 manage.py migrate
# to show all migrations you can run the command "python3 manage.py showmigration"
# to save the changes into database tables type below command
# python3 manage.py migrate myapp --plan
# confirm save type
# python3 manage.py migrate myapp
# and to rename in sql type below command
# python3 manage.py sqlmigrate myapp  0003

# get one by id run below command:
# Menu.objects.get()
# To get one according to your choices attribute we can use filter function
# Menu.objects.filter(email = "muhayimana21@gmail.com")
# create super user
# python3 manage.py createsuperuser
# and follows the rules
 

