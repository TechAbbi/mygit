from django.db import models

# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100, unique=True)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=1000,
                                default="https://static.wixstatic.com/media/bf242e_6133b4ae6a104cc2b50d70179f35efea~mv2.jpg/v1/fill/w_500,h_376,al_c,lg_1,q_80,enc_auto/food-placeholder.jpg")
