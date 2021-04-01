from django.db import models

# Create your models here.

class MovieIMDB(models.Model):
    """
    Model to save the data of an IMDB movie object
    """

    title = models.TextField()
    year = models.IntegerField()
    rating = models.CharField(max_length=20)
    genre = models.TextField()
    runtime = models.TextField()
    certificate = models.TextField()
    directors = models.TextField()
    stars = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.movie_title


