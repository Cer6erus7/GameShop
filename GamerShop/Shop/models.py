from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-price']
