from django.db import models

class reservations(models.Model):
    
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    time_log = models.DateField(auto_now_add=True)