from django.db import models

# Create your models here.


class Rate(models.Model):
    title = models.CharField(max_length=35, unique=True)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='rate-image/', verbose_name='rate-image')
    price = models.IntegerField()
    term = models.CharField(max_length=55)
    create_ed = models.DateTimeField(auto_now=True)
    update_ed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Personal(models.Model):
    name = models.CharField(max_length=75)
    age = models.SmallIntegerField()
    experience = models.TextField()
    ebalo = models.ImageField(upload_to='roga/', verbose_name='personal-image')

    def __str__(self):
        return self.name
