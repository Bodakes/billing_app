from django.db import models

class productList(models.Model):
     name=models.CharField(max_length=105)
     price=models.CharField(max_length=105) 
     description=models.CharField(max_length=105)
     qty=models.CharField(max_length=105)
