import requests

from api_tests import data, configuration


# Иван Самкин, 20-я когорта - Финальный проект. Инженер по тестированию плюс
def create_order():
    create_order_response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=data.create_order_body
    )
    track = create_order_response.json()["track"]
    return track


def get_order_by_track():
    get_order_by_track_response = requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
        params={"t": create_order()}
    )
    return get_order_by_track_response


def test_get_order_by_track_code_200():
    response = get_order_by_track()
    assert response.status_code == 200
