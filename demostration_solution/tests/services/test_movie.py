from unittest import mock

import pytest

from pytest_lazyfixture import lazy_fixture


class MovieNotFound(Exception):
    pass


@pytest.mark.parametrize(
    'data',
    (
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

    )
)
def test_get_one(movie_service, data):
    movie_service.dao.get_one.return_value = data
    assert movie_service.get_one(data['id']) == data


def test_get_one_with_error(movie_service):
    movie_service.dao.get_one.side_effect = MovieNotFound

    with pytest.raises(MovieNotFound):
        movie_service.get_one(0)


@pytest.mark.parametrize('length, data', ((2, lazy_fixture('movies_list'),),),)
def test_get_all(movie_service, length, data):
    movie_service.dao.get_all.return_value = data
    test_result = movie_service.get_all()

    assert isinstance(test_result, list)
    assert len(test_result) == length
    assert test_result == data


@pytest.mark.parametrize(
    'origin_data, modif_data',
    (
            (
                    {
                        'id': 1,
                        'title': 'test',
                        'description': 'test',
                        'trailer': 'test',
                        'year': 'test',
                        'rating': 'test',
                        'genre_id': 'test',
                        'director_id': 'test'
                    },
                    {
                        'id': 1,
                        'title': 'changed',
                        'description': 'changed',
                        'trailer': 'changed',
                        'year': 'changed',
                        'rating': 'changed',
                        'genre_id': 'changed',
                        'director_id': 'changed'

                    },
            ),
    )
)
def test_partially_update(movie_service, origin_data, modif_data):
    movie_service.dao.get_one.return_value = origin_data
    movie_service.partially_update(modif_data)

    movie_service.dao.get_one.assert_called_once_with(origin_data['id'])
    movie_service.dao.update.assert_called_once_with(modif_data)


@pytest.mark.parametrize(
    'origin_data, modif_data',
    (
            (
                    {
                        'id': 1,
                        'title  ': 'test'
                    },
                    {
                        'id': 1,
                        'wrong_field': 'wrong_data'
                    },
            ),
    )
)
def test_partially_update_with_wrong_fields(movie_service, origin_data, modif_data):
    movie_service.dao.get_one.return_value = origin_data
    movie_service.partially_update(modif_data)

    movie_service.dao.update.assert_called_once_with(origin_data)


@pytest.mark.parametrize('movie_id', (1,))
def test_delete(movie_service, movie_id):
    movie_service.delete(movie_id)
    movie_service.dao.delete.assert_called_once_with(movie_id)


@pytest.mark.parametrize(
    'movie_data',
    (
            (
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
            ),
    )
)
def test_update(movie_service, movie_data):
    movie_service.update(movie_data)
    movie_service.dao.update.assert_called_once_with(movie_data)
