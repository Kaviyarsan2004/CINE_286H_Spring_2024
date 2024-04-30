# In a Python script, e.g., populate_movies.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcrm.settings')
django.setup()

from movies.models import Movie

def add_movies():
    movies_data = [
        {
            'name': 'Movie 1',
            'description': 'Description of Movie 1',
            'image': 'movie1.jpg',  # Replace with the actual image file path
        },
        {
            'name': 'Movie 2',
            'description': 'Description of Movie 2',
            'image': 'movie2.jpg',
        },
        {
            'name': 'Movie 3',
            'description': 'Description of Movie 3',
            'image': 'movie3.jpg',
        },
        {
            'name': 'Movie 4',
            'description': 'Description of Movie 4',
            'image': 'movie4.jpg',
        },
        {
            'name': 'Movie 5',
            'description': 'Description of Movie 5',
            'image': 'movie5.jpg',
        },
    ]

    for movie_data in movies_data:
        movie = Movie.objects.create(
            name=movie_data['name'],
            description=movie_data['description'],
            image=movie_data['image'],
        )
        movie.save()

if __name__ == '__main__':
    add_movies()
