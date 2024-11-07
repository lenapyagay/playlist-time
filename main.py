## project_4

# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * многострочная строка
#   * словарь
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any


import random
from datetime import timedelta

playlist_e = """
Sunday 5:09
Why Does My Heart Feel so Bad? 4.23
Everlong 3.25
To Let Myself Go 2.34
Golden 2.56
Daisuke 2.41
Miami 3.31
Chill Bill Lofi 2.05
The Perfect Girl 1.48
Resonance 3.32
"""

playlist_b = {
  'Портофино': 3.32,
  'Снег': 4.35,
  'Попытка №5': 3.23,
  'Тополиный Пух': 3.53,
  'Если хочешь остаться': 4.48,
  'Зеленоглазое такси': 5.52,
  'Ты не верь слезам': 3.1,
  'Nowhere to Run': 2.58,
  'Салют, Вера': 4.44,
  'Улетаю': 3.24,
  'Опять метель': 3.37,
  }

# Функция для преобразования времени в формате "минуты.секунды" или "минуты:секунды" в объект timedelta
def parse_time(time_str):
    separator = ':' if ':' in time_str else '.'
    minutes, seconds = map(int, time_str.split(separator))
    return timedelta(minutes=minutes, seconds=seconds)

# Функция для преобразования многострочного текста в словарь с песнями
def parse_text_playlist(text_playlist):
    playlist = {}
    for line in text_playlist.strip().splitlines():
        parts = line.rsplit(" ", 1)
        if len(parts) == 2:
            name, time = parts
            playlist[name] = parse_time(time)
    return playlist

# Основная функция для вычисления общей длительности случайных песен
def get_duration(playlist, n):
    # Определяем, является ли плейлист строкой или словарем
    if isinstance(playlist, str):
        playlist = parse_text_playlist(playlist)  # Преобразуем текст в словарь
    elif isinstance(playlist, dict):
        # Преобразуем значение времени в формате "минуты.секунды" в timedelta
        playlist = {name: parse_time(f"{int(duration)}:{int(duration % 1 * 100)}") for name, duration in playlist.items()}
    
    # Проверка, чтобы n не превышало количество песен
    if n > len(playlist):
        n = len(playlist)
    
    # Выбираем случайные песни и суммируем их длительность
    selected_songs = random.sample(list(playlist.values()), n)
    total_duration = sum(selected_songs, timedelta())
    
    return total_duration  # Вернуть как timedelta


nuber_of_songs1 = int(input("Введите количество песен:"))
nuber_of_songs2 = int(input("Введите количество песен:"))
# Тестирование функции
print("Общее время {n1} случайных песен (playlist_e):".format(n1=nuber_of_songs1), get_duration(playlist_e, nuber_of_songs1))
print("Общее время {n2} случайных песен (playlist_b):".format(n2=nuber_of_songs2), get_duration(playlist_b, nuber_of_songs2))


