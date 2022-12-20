from django.db import models

# Create your models here.

class detail(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.IntegerField()
    Date_time  = models.DateField(auto_now=True)

    Purpose = models.CharField(max_length=250)
    class Meta:  
        db_table = "Details" 