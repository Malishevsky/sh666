from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.text import slugify


class Auto(models.Model):
    firm = models.CharField(max_length=100, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    volume = models.FloatField(verbose_name='Обьём')
    image = models.ImageField(upload_to='infocar/%Y-%m-%d/',blank='True',null='True',verbose_name='Фото')
    engine = models.ForeignKey('Engine', verbose_name='Двигатель', on_delete=models.CASCADE)
    transmission = models.ForeignKey('Transmission', verbose_name='Трансмиссия', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    complectations = models.ManyToManyField('Complectation', verbose_name='Комплектация', blank='True', null='True')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self,**kwargs):
        return  reverse('poster',kwargs={'post_slug': self.slug})
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.firm}-{self.model}-{self.price}')
        super(Auto, self).save(*args, **kwargs)

    def __str__(self):
        return self.firm + ' ' + self.model

    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'
        ordering = ['-price']


class Engine(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип двигателя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name_plural = 'Двигатели'
        verbose_name = 'Двигатель'

    def __str__(self):
        return self.name


class Transmission(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип трансмиссии')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name_plural = 'Трансмиссии'
        verbose_name = 'Трансмиссия'

    def __str__(self):
        return self.name


class Complectation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Комплектация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Комплектация'
        verbose_name = 'Комплектация'
# Create your models here.
