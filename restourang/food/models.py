from django.db import models

food_category = (
    ('pizza', 'pizza'),
    ('burger', 'burger'),
    ('pasta', 'pasta'),
    ('fries', 'fries'),
)


class Food(models.Model):
    category = models.CharField(max_length=6, choices=food_category)
    image = models.ImageField(upload_to='food_img/')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=105)
    price = models.IntegerField()

    def __str__(self):
        return self.name 