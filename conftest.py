import pytest
import json

import requests_mock


@pytest.fixture()
def mock_hero():
    with open("data_heroes_dump.json") as hero:
        return json.load(hero)


@pytest.fixture()
def mock_requests(mock_hero):
    with requests_mock.Mocker() as m:
        m.get("https://akabab.github.io/superhero-api/api/all.json", json=mock_hero)
        yield m


@pytest.fixture()
def mock_request_id(mock_hero):
    def find_hero(id):
        with requests_mock.Mocker() as m:
            hero_data = next(item for item in mock_hero if item["id"] == id)
            m.get(
                f"https://akabab.github.io/superhero-api/api/id/{id}.json",
                json=hero_data,
            )
            return hero_data

    return find_hero
