import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.41 Safari/537.36'
}

json_list = []

cities = [
    "Київ",
    "Харків",
    "Одеса",
    "Дніпро",
    "Львів",
    "Запоріжжя",
    "Кривий Ріг",
    "Миколаїв",
    "Маріуполь",
    "Вінниця",
    "Херсон",
    "Полтава",
    "Чернігів",
    "Черкаси",
    "Житомир",
    "Суми",
    "Хмельницький",
    "Рівне",
    "Тернопіль",
    "Івано-Франківськ",
    "Луцьк",
    "Ужгород",
    "Кам'янець-Подільський",
    "Сімферополь",
    "Мелітополь",
    "Бердянськ",
    "Євпаторія",
    "Донецьк",
    "Лисичанськ",
    "Кременчук",
    "Єнакієве",
    "Луганськ",
    "Сєвєродонецьк",
    "Макіївка",
    "Чернівці",
    "Хуст",
    "Мукачево",
    "Дрогобич",
    "Мар'їнка",
    "Слов'янськ",
    "Краматорськ",
    "Жмеринка",
    "Ірпінь",
    "Вишгород",
    "Біла Церква",
    "Умань",
    "Славутич",
    "Бровари",
    "Макарів",
    "Васильків",
    "Ковель",
    "Конотоп",
    "Шостка",
    "Охтирка",
    "Прилуки",
    "Ладижин",
    "Могилів-Подільський",
    "Бершадь",
    "Збараж",
    "Козятин",
    "Лубни",
    "Гадяч",
    "Золотоноша",
    "Пирятин",
    "Чорнобиль",
    "Енергодар",
    "Бердичів",
    "Путивль",
    "Кременець",
    "Білогір'я",
    "Сіверськ",
    "Миргород",
    "Берегове",
    "Виноградів",
    "Свалява",
    "Рахів",
    "Іршава",
]


city_input = input('Введіть назву міста, погоду якого ви хочете побачити: ')

# Find the city in the list and encode it
if city_input in cities:
    encoded_city = quote(city_input, safe='')
    weather_count = f'%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-{encoded_city}'
    url = f'https://ua.sinoptik.ua/{weather_count}'
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    cards = soup.find_all('div', class_='main')

    for card in cards:
        date = card.find('p', class_='date').text.strip()
        month = card.find('p', class_='month').text.strip()
        pogoda_elem = card.find('div', class_='weatherIco')
        day_elem = card.find('a', class_='day-link')
        monday_day_elem = card.find('p', class_='day-link')
        min_temp = card.find('div', class_='min').find('span').text
        max_temp = card.find('div', class_='max').find('span').text
        if pogoda_elem and day_elem:
            pogoda = pogoda_elem.get('title')
            day = day_elem.text.strip()


            json_data = {
            'Дата':f'{day}, {date} {month}',
            'Погода':f'{pogoda}',
            'Мін.градусів': f'{min_temp}',
            'Макс.градусів': f'{max_temp}'
            }

            json_list.append(json_data)

        else:
            day = monday_day_elem.text.strip()
            pogoda = pogoda_elem.get('title')
            json_data = {
                'Дата': f'{day}, {date} {month}',
                'Погода': f'{pogoda}',
                'Мін.градусів': f'{min_temp}',
                'Макс.градусів': f'{max_temp}'
            }

            json_list.append(json_data)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(json_list, file, ensure_ascii=False, indent=4)
else:
    print('Місто не знайдено в списку.')





