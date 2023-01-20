from django.db import models
from django.core.validators import RegexValidator
import uuid
import os

# Create your models here.


class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Dish(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('image/dishes', filename)

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    desc = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return f'{self.name}'


class Gallery(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('image/gallery', filename)

    photo = models.ImageField(upload_to=get_file_name)
    desc = models.CharField(max_length=100, blank=True)
    is_visible = models.BooleanField(default=True)


class UserReservation(models.Model):
    phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[ -]?){7}$', message='')
    e_mail_validator = \
        RegexValidator(regex=r'[a-zA-Z0-9][a-zA-Z0-9_\-]*(\.[a-zA-Z0-9_\-]+)?@([a-zA-Z0-9_]|\-)+(\.[a-zA-Z0-9_]{1,10})+')
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    e_mail = models.CharField(max_length=50, validators=[e_mail_validator])
    persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=250, blank=True)
    date = models.DateField(auto_now_add=True)
    date_time_order = models.DateTimeField(auto_now=True)
    manager_date_processed = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.name} {self.phone}: {self.message[:20]}'
