from django.db import models

# Create your models here.

class examp(models.Model):
    name=models.CharField(max_length=50,primary_key=True)
    
    class Meta:
        db_table="TEAM"