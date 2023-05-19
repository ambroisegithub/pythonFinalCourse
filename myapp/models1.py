from django.db import models

class Logger(models.Model):
    
    first_Name = models.CharField(max_length=60)
    last_Name = models.CharField(max_length=70)
    Email = models.EmailField()
    time_Log = models.DateTimeField(help_text="Enter exact Time!")
    
    