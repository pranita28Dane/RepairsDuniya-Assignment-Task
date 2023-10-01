from django.db import models

class User(models.Model):
    #id = models.PositiveIntegerField(primary_key=True)  
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = "djangodb" 

    def __str__(self):
        return self.name