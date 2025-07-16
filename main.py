import requests
import json
from typesettings import Gender

#response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
#response_pretty = json.dumps(response.json(), indent = 4)
#response = requests.get('https://akabab.github.io/superhero-api/api//id/999.json')
#print(response.status_code)
def load_heroes():
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    json_data = response.json()
    return json_data

def filtered_gender_and_work(gender: str, check: bool):
    heroes = load_heroes()
    valid_gender = {genders.value for genders in Gender}
    if gender not in valid_gender:
        raise ValueError(
            f"Недопустимое значение пола: '{gender}'. "
            f"Допустимые значения: {', '.join(valid_gender)}"
        )
    if isinstance(check, bool) == False:
        raise ValueError(
            "Параметр check должен быть True/False"
        )
    filtered_gender = [item for item in heroes if item['appearance']['gender'] == gender]
    if check == True:
        filter_both = [item for item in filtered_gender if item['work']['occupation'] != '-' or item['work']['base'] != '-']
    else:
        filter_both = [item for item in filtered_gender if item['work']['occupation'] == '-' and item['work']['base'] == '-']
    return filter_both


def get_height_cm(hero: dict):
    height = hero['appearance'].get('height')
    height_str = height[1]
    if 'meter' in height_str:
        return int(float(height_str.split()[0]) * 100)
    else:
        return int(height_str.split()[0])

def tallest_hero_information(gender: str, check: bool):
    heroes = filtered_gender_and_work(gender, check)
    tallest_hero = max(heroes, key=get_height_cm)
    tallest_hero = tallest_hero['id']
    hero_information = requests.get(f'https://akabab.github.io/superhero-api/api/id/{tallest_hero}.json')
    return hero_information.json()

def main():
  result = tallest_hero_information("Female", True)
  print(json.dumps(result, indent=4))
if __name__ == "__main__":
    main()