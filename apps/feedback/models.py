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


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, related_name='review', on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='review-image-kor/')


class Comment(models.Model):
    body = models.TextField(verbose_name='Description')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    files = models.FileField(upload_to='comment_files/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}, {self.body}'