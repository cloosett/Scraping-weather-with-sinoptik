# Scraping-weather-with-sinoptik

Цей Python скрипт призначений для отримання інформації про погоду з веб-сайту Sinoptik.ua для вказаного користувачем міста. Скрипт використовує бібліотеки requests, BeautifulSoup та json для отримання, парсингу та збереження даних.

Використання
Запустіть скрипт.
Введіть назву міста, для якого ви хочете отримати погоду.
Скрипт перевірить наявність міста в списку доступних міст і, якщо знайдено, витягне та збереже інформацію про погоду у файл data.json.

Залежності
Переконайтеся, що встановлені необхідні залежності. Ви можете встановити їх за допомогою наступної команди:
pip install requests beautifulsoup4

Дані та Файл JSON
Отримана інформація про погоду для введеного міста буде збережена у файлі data.json. Файл містить дані у форматі JSON та оформлений з інтервалами для легшого читання.

Важливі Зауваження
Скрипт використовує агента користувача (User-Agent) для імітації запитів браузера і уникнення блокування.
В разі введення міста, яке не знаходиться в списку доступних міст, виведеться повідомлення про невдалий пошук.
Настроюйте та використовуйте скрипт залежно від своїх потреб!
