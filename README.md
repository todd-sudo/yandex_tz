# Тестовое задание (Яндекс)


### Настройка окружения

#### 1. Склонировать проект
#### 2. Создать виртуальное окружение в корне проекта: `python3 -m venv venv && source venv/bin/activate`
#### 3. Установить зависимости из `requirements.txt`: `pip install -r requirements.txt`


### Отправка постов в телеграм канал(link: https://t.me/testchanya)

<br>

#### 1. Создать файл .env в директории `third_task/`. Содержимое файла:

```env
TOKEN_BOT=токен_бота_в_telegram
```

#### 2. Запуск:
    
``` bash
python third_task/main.py
```

#### 3. Чтобы проверить работоспособность, нужно перейти в файл настроек `third_task/config.py` и прописать название канала без `@`
#### Предварительно нужно добавить туда своего бота и дать ему права администратора. Так же можно воспользоваться предложенным каналом. Найти его можно по адресу: https://t.me/testchanya . Просто перейдите по ссылке и запустите скрипт)

<br>

### Отправка постов в телеграм канал(link: https://t.me/testchanya)


### Парсинг .csv файла

#### 1. Перейти в директорию `first_task`
#### 2. Запустить файл `main.py`
#### 3. Скрипт потребует путь до входного файла (https://disk.yandex.ru/d/ZTnv3LiUeqEK5A)
#### 4. На выходе получиться файл `data.csv`