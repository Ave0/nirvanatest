from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from backend.models import MovieIMDB
from rest_framework import viewsets, filters, permissions
from .serializers import MovieIMDBSerializer
from contextlib import contextmanager
from bs4 import BeautifulSoup
import requests

ENDPOINT = "https://www.imdb.com/search/title/"
BASE_URL = f"{ENDPOINT}?groups=top_2000&sort=user_rating,desc&start="


@contextmanager
def ignored(*exceptions):
    """
    Function to wrap any exception
    """
    try:
        yield
    except exceptions:
        pass


def process_director_stars(directors_stars):
    """
    Function to process and clean the directors and starts
    :params: string directors_stars unprocessed
    :return : directors, start  string.

    """
    directors_stars = directors_stars.split("|")
    # Retriving the director and removing the tag
    directors = (directors_stars[0].split(":")[1]).strip()
    # Removing also new lines
    directors = directors.replace("\n", " ")

    # Retriving the starts and removing the tag
    stars = (directors_stars[1].split(":")[1]).strip()
    # Removing also new lines
    stars = stars.replace("\n", " ")
    return directors, stars


def parse_movie_soup(soup_movie):
    """
    Function to process a soup movie element and save
    the movie in the django models.
    :params: soup object of a specific movie
    """

    # Initialize variables

    title = ""
    year = 0
    rating = ""
    genre = ""
    runtime = ""
    certificate = "Not rated"
    directors = ""
    stars = ""
    description = ""

    # Start processing
    with ignored(Exception):
        header = soup_movie.find('h3', class_='lister-item-header')
        title = (header.find("a", href=True).text).strip()
        year = header.find(
            'span', class_='lister-item-year text-muted unbold').text
        # Removing parentheses and convert to int
        year = int(year[1:-1])

    if not isinstance(year, int):
        year = 0

    with ignored(Exception):
        rating = (
            soup_movie.find(
                'div',
                class_='inline-block ratings-imdb-rating').text).strip()

    with ignored(Exception):
        genre = (soup_movie.find('span', class_='genre').text).strip()

    with ignored(Exception):
        runtime = (soup_movie.find('span', class_='runtime').text).strip()

    with ignored(Exception):
        certificate = (
            soup_movie.find(
                'span',
                class_='certificate').text).strip()

    with ignored(Exception):
        directors_starts = (soup_movie.find('p', class_='').text).strip()
        directors, stars = process_director_stars(directors_starts)

    with ignored(Exception):
        description = (
            soup_movie.find_all(
                'p', class_='text-muted')[1].text).strip()

    # Creating movie object
    movie = MovieIMDB.objects.create(
        title=title,
        year=year,
        rating=rating,
        genre=genre,
        runtime=runtime,
        certificate=certificate,
        directors=directors,
        stars=stars,
        description=description
    )
    # Saving movie object
    movie.save()


def get_movies():
    """
    Entry function to get the data from IMDB page
    iterate over the pages and process the movie elements.
    """
    # Clean any objects we have saved.
    MovieIMDB.objects.all().delete()

    for i in range(0, 2000, 50):
        current_url = BASE_URL + str(i)
        page = requests.get(current_url)

        soup = BeautifulSoup(page.text, 'html.parser')
        movie_elements = soup.find_all(
            "div", {"class": "lister-item mode-advanced"})
        for movie in movie_elements:
            parse_movie_soup(movie)


# @login_required(login_url='/backend/admin/login.html')
def UpdateView(request):
    get_movies()
    return HttpResponse("Update sucessfully")


# Start serializer views


class MovieIMDBserViewSet(viewsets.ModelViewSet):
    search_fields = ['directors', 'description']
    filter_backends = (filters.SearchFilter,)
    print(f"El valor search_fields es {search_fields}")
    queryset = MovieIMDB.objects.all()
    serializer_class = MovieIMDBSerializer
    # permission_classes = [permissions.IsAuthenticated]
