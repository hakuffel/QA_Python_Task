import pytest
from src.main import filtered_gender_and_work, get_height_cm, tallest_hero_information


@pytest.mark.positive
def test_filter_female_with_work():
    result = filtered_gender_and_work("Female", True)
    assert len(result) > 0
    for hero in result:
        assert hero["appearance"]["gender"] == "Female"
        assert hero["work"]["occupation"] != "-" or hero["work"]["base"] != "-"


@pytest.mark.positive
def test_filter_male_without_work():
    result = filtered_gender_and_work("Male", False)
    for hero in result:
        assert hero["appearance"]["gender"] == "Male"
        assert hero["work"]["occupation"] == "-"
        assert hero["work"]["base"] == "-"


@pytest.mark.positive
def test_unknown_without_work():
    result = filtered_gender_and_work("-", False)
    for hero in result:
        assert hero["appearance"]["gender"] == "-"
        assert hero["work"]["occupation"] == "-"
        assert hero["work"]["base"] == "-"


@pytest.mark.positive
def test_unknown_with_work():
    result = filtered_gender_and_work("-", True)
    for hero in result:
        assert hero["appearance"]["gender"] == "-"
        assert hero["work"]["occupation"] != "-" or hero["work"]["base"] != "-"


@pytest.mark.negative
def test_invalid_gender():
    with pytest.raises(ValueError):
        filtered_gender_and_work("Invalid", True)


@pytest.mark.negative
def test_invalid_check_work():
    with pytest.raises(ValueError):
        filtered_gender_and_work("Male", "pupupu")


@pytest.mark.positive
def test_get_height_cm():
    hero_cm = {"appearance": {"height": ["6'0", "180 cm"]}}
    assert get_height_cm(hero_cm) == 180


@pytest.mark.positive
def test_get_height_cm_if_meters():
    hero_meters = {"appearance": {"height": ["5'5", "1.65 meters"]}}
    assert get_height_cm(hero_meters) == 165


@pytest.mark.positive
def test_tallest_hero_female():
    result = tallest_hero_information("Female", True)
    assert result["appearance"]["gender"] == "Female"


@pytest.mark.positive
def test_tallest_hero_male():
    result = tallest_hero_information("Male", True)
    assert result["appearance"]["gender"] == "Male"


@pytest.mark.positive
def test_tallest_hero_unknown():
    result = tallest_hero_information("-", True)
    assert result["appearance"]["gender"] == "-"


@pytest.mark.negative
def test_tallest_hero_none_gender():
    with pytest.raises(ValueError):
        tallest_hero_information(None, True)


@pytest.mark.negative
def test_tallest_hero_none_work():
    with pytest.raises(ValueError):
        tallest_hero_information("Male", None)
