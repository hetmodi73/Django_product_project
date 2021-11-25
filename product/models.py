from django.db import models

# Create your models here.

class products(models.Model):
    name=models.CharField(max_length=30)
    weight=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return f"{self.name}"
