1. Скачиваем модель:
https://drive.google.com/file/d/19tc6mQlW3mUoJNV6cUJREacYMHrI0PNs/view?usp=drive_link
2. Распаковываем ее в ./model
3. Запускаем бекенд:
  1. Переходим в папку ./backend
  2. Создаем виртуальное окружение: ```python -m venv venv```
  3. Активируем виртуальное окружение: ```./venv/Scripts/Activate```
  4. Устанавливаем модули: ```pip install -r requirements.txt```
  5. Запускаем: ```flask run```
4. Запускаем фронтенд:
  1. Переходим в папку ./demo
  2. Открываем index_bundle.html в браузере
  3. Или запускаем любой удобный сервер (например https://github.com/static-web-server/static-web-server/)
  ```sws -d .```
