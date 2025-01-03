# Алгоритм работы текстового квеста

## 1. Инициализация игры
1. Загрузка данных
   - Загрузка сцен и диалогов из story/scenes.py
   - Загрузка предметов из data/items.py
   - Инициализация параметров игрока (здоровье = 100, пустой инвентарь)

2. Создание начального состояния
   - Установка текущей сцены на начальную
   - Инициализация флагов прогресса
   - Подготовка системы сохранения

## 2. Основной игровой цикл
```
ПОКА игра_активна:
    1. Отобразить текущую сцену
       - Показать описание локации
       - Показать состояние игрока (здоровье, инвентарь)
       - Вывести доступные действия

    2. Получить действие игрока
       - Проверить валидность ввода
       - Обработать специальные команды (сохранение, выход)

    3. Обработать действие
       - Изменить состояние игрока (здоровье, инвентарь)
       - Обновить игровые флаги
       - Определить следующую сцену

    4. Проверить условия завершения
       - Проверить здоровье игрока
       - Проверить достижение концовки
```

## 3. Система инвентаря
1. Структура предмета:
```python
{
    "id": "item_id",
    "name": "Название",
    "description": "Описание",
    "usable": True/False,
    "effect": {
        "type": "health/story",
        "value": значение
    }
}
```

2. Операции с инвентарём:
   - Добавить предмет (проверка лимита слотов)
   - Удалить предмет
   - Использовать предмет
   - Показать инвентарь

## 4. Система здоровья
1. Изменение здоровья:
   - Получение урона (проверка на смерть)
   - Лечение (не больше максимума)
   - Обновление статуса

## 5. Система сцен
1. Структура сцены:
```python
{
    "id": "scene_id",
    "description": "Описание сцены",
    "choices": [
        {
            "text": "Текст выбора",
            "requirements": {
                "item": "требуемый_предмет",
                "health": минимальное_здоровье
            },
            "effects": {
                "health": изменение_здоровья,
                "items": [добавить/удалить],
                "next_scene": "id_следующей_сцены"
            }
        }
    ]
}
```

## 6. Обработка концовок
1. Типы завершения игры:
   - Смерть персонажа (здоровье = 0)
   - Хорошая концовка
   - Нейтральная концовка
   - Плохая концовка

2. Действия при завершении:
   - Показать итоговое описание
   - Вывести статистику игры
   - Предложить начать заново

## 7. Система сохранения
1. Сохраняемые данные:
   - Текущая сцена
   - Состояние игрока
   - Инвентарь
   - Игровые флаги

2. Формат сохранения:
```python
{
    "player": {
        "health": текущее_здоровье,
        "inventory": [предметы]
    },
    "game_state": {
        "current_scene": "id_сцены",
        "flags": {флаги_прогресса}
    }
}
```

## 8. Обработка ошибок
1. Проверки:
   - Валидация ввода игрока
   - Проверка существования сцен
   - Проверка условий для действий
   - Контроль целостности данных

2. Действия при ошибках:
   - Вывод понятного сообщения
   - Возврат к предыдущему состоянию
   - Логирование ошибок
