from django.db import models

# Create your models here.

class CarsModel(models.Model):
    make=models.CharField(max_length=20, default=0)
    model_num=models.CharField(max_length=30, default=0)
    year=models.IntegerField(default=0)
    cartype=models.CharField(max_length=20,default=0)
    fuel_type=models.CharField(max_length=20,default=0)
    Gas_Milage=models.CharField(max_length=20,default=0)
    PRICE=models.FloatField(default=0)
    image=models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.model_num+ self.fuel_type
