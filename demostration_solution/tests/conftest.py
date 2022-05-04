from unittest import mock
from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.director import DirectorService
from demostration_solution.service.genre import GenreService
from demostration_solution.service.movie import MovieService


@pytest.fixture
def director_dao():
    dao = DirectorDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


@pytest.fixture
def director_service(director_dao):
    return DirectorService(dao=director_dao)


@pytest.fixture
def directors_list():
    return [{'id': 1, 'name': mock.ANY}, {'id': 2, 'name': mock.ANY}, ]


@pytest.fixture
def genre_dao():
    dao = GenreDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


@pytest.fixture
def genre_service(genre_dao):
    return GenreService(dao=genre_dao)


@pytest.fixture
def genres_list():
    return [{'id': 1, 'name': mock.ANY}, {'id': 2, 'name': mock.ANY}, ]


@pytest.fixture
def movie_dao():
    dao = MovieDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


@pytest.fixture
def movie_service(movie_dao):
    return MovieService(dao=movie_dao)


@pytest.fixture
def movies_list():
    return [
        {
            'id': 1,
            'title': mock.ANY,
            'description': mock.ANY,
            'trailer': mock.ANY,
            'year': mock.ANY,
            'rating': mock.ANY,
            'genre_id': mock.ANY,
            'director_id': mock.ANY
        },
        {
            'id': 2,
            'title': mock.ANY,
            'description': mock.ANY,
            'trailer': mock.ANY,
            'year': mock.ANY,
            'rating': mock.ANY,
            'genre_id': mock.ANY,
            'director_id': mock.ANY
        },
    ]
