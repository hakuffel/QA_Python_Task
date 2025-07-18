import pytest
import json

import requests_mock
from pathlib import Path


@pytest.fixture()
def mock_hero():
    project_root = Path(__file__).parent
    data_path = project_root / "tests" / "data_heroes_dump.json"
    if not data_path.exists():
        data_path = Path("data_heroes_dump.json")
    with open(data_path) as hero:
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
