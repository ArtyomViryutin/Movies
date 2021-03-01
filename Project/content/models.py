from django.db import models

from users.models import User
from .validators import validate_year

class Genre(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30, unique=True)



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30, unique=True)



class Title(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(validators=[validate_year],db_index=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='category_titles', null=True)
    genre = models.ManyToManyField(Genre, related_name='genre_titles',
                                   blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('year',)
