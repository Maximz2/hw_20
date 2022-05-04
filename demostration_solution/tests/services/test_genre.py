from unittest import mock

import pytest

from pytest_lazyfixture import lazy_fixture


class GenreNotFound(Exception):
    pass


@pytest.mark.parametrize('data', ({'id': 1, 'name': mock.ANY},))
def test_get_one(genre_service, data):
    genre_service.dao.get_one.return_value = data
    assert genre_service.get_one(data['id']) == data


def test_get_one_with_error(genre_service):
    genre_service.dao.get_one.side_effect = GenreNotFound

    with pytest.raises(GenreNotFound):
        genre_service.get_one(0)


@pytest.mark.parametrize('length, data', ((2, lazy_fixture('genres_list'),),),)
def test_get_all(genre_service, length, data):
    genre_service.dao.get_all.return_value = data
    test_result = genre_service.get_all()

    assert isinstance(test_result, list)
    assert len(test_result) == length
    assert test_result == data


@pytest.mark.parametrize('origin_data, modif_data', (({'id': 1, 'name': 'test'}, {'id': 1, 'name': 'changed_name'},),))
def test_partially_update(genre_service, origin_data, modif_data):
    genre_service.dao.get_one.return_value = origin_data
    genre_service.partially_update(modif_data)

    genre_service.dao.get_one.assert_called_once_with(origin_data['id'])
    genre_service.dao.update.assert_called_once_with(modif_data)


@pytest.mark.parametrize('origin_data, modif_data', (({'id': 1, 'name': 'test'}, {'id': 1, 'wrong_field': 'wrong_data'},),))
def test_partially_update_with_wrong_fields(genre_service, origin_data, modif_data):
    genre_service.dao.get_one.return_value = origin_data
    genre_service.partially_update(modif_data)

    genre_service.dao.update.assert_called_once_with(origin_data)


@pytest.mark.parametrize('genre_id', (1,))
def test_delete(genre_service, genre_id):
    genre_service.delete(genre_id)
    genre_service.dao.delete.assert_called_once_with(genre_id)


@pytest.mark.parametrize('genre_data', (({'id': mock.ANY, 'name': mock.ANY}),))
def test_update(genre_service, genre_data):
    genre_service.update(genre_data)
    genre_service.dao.update.assert_called_once_with(genre_data)
