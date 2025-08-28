import pytest
from API import Yougile

# Тестовые данные
base_url = Yougile('https://yougile.com/')
token = 'ВВЕДИТЕ ПОЛУЧЕННЫЙ ТОКЕН В СООБЩЕНИИ'
id_project = "ce4a2a83-98f0-4924-9924-05700508ce97"
id_project_neg = "ce4a2a83-98f0-4924-9924-05700508ce9"

# Позитивные проверки


@pytest.mark.positive
def test_сreate_pos():
    new_simple = Yougile.create(base_url, token, 'Тест 1')
    assert new_simple[0] == 201


def test_change_pos():
    change = Yougile.change(base_url, token, 'Тест 1 Новый', id_project)
    assert change[0] == 200


def test_get_by_id_pos():
    get_by_id = Yougile.get_by_id(base_url, token, id_project)
    assert get_by_id[0] == 200
    print(get_by_id[1])


# Негативные проверки


@pytest.mark.negative
def test_сreate_neg():
    create_new = Yougile.create(base_url, token, '')
    assert create_new[0] == 400


def test_change_neg():
    change = Yougile.change(base_url, token, '', id_project)
    assert change[0] == 400


def test_get_by_id_neg():
    get_by_id = Yougile.get_by_id(base_url, token, id_project_neg)
    assert get_by_id[0] == 404
