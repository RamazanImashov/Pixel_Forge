from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Review(models.Model):
    rating = models.PositiveSmallIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    descriptions = models.TextField()
    image = models.ImageField(upload_to='review-image/', verbose_name='review-image', blank=True)

    def __str__(self):
            return f'{self.author} {self.rating}'