from django.db import models

class MenuTemplates(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    def __str__(self):
        return self.name