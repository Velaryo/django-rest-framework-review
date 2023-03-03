from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.CharField(max_length=50)
    image = models.TextField()
    country = models.CharField(max_length=50)
    duration = models.IntegerField()
    price = models.FloatField()
    #todo create y update 100% automático
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'movies'