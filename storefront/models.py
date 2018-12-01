from django.db import models

class inventory(models.Model):
    itemName = models.CharField(max_length = 1000)
    price = models.FloatField(max_length = 50)
    itemIcon = models.CharField(max_length = 1000)

    def __str__(self):
        return self.itemName + ' for $' + str(self.price)
