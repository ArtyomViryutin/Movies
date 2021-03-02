from django.db import models

from users.models import User

from .validators import validate_score, validate_year


class Genre(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        ordering = ('-id',)


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        ordering = ('-id',)


class Title(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(validators=[validate_year], db_index=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='category_titles', null=True)
    genre = models.ManyToManyField(Genre, related_name='genre_titles',
                                   blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('year',)


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.CharField(max_length=300)
    score = models.IntegerField(validators=[validate_score])
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)

