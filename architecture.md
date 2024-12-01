# Архитектура проекта текстового квеста

## Общее описание
Веб-приложение построено на архитектуре клиент-сервер без использования внешних баз данных. Все данные хранятся в файловой системе в формате JSON.

## Backend (Python/FastAPI)
### Компоненты
- RESTful API для обработки игровой логики
- Файловая система для хранения:
  - Сцен и диалогов
  - Предметов и их свойств
  - Состояний игры
- Обработка игровых состояний
- Валидация действий игрока

### Структура данных
```
backend/
├── app/
│   ├── api/
│   │   └── endpoints/
│   │       ├── game.py        # Эндпоинты игровой логики
│   │       └── player.py      # Управление игроком
│   ├── core/
│   │   ├── config.py         # Конфигурация приложения
│   │   └── game_state.py     # Управление состоянием
│   ├── game/
│   │   ├── engine.py         # Игровой движок
│   │   ├── inventory.py      # Система инвентаря
│   │   └── scenes.py         # Обработка сцен
│   └── data/
│       ├── items/            # JSON файлы предметов
│       ├── scenes/           # JSON файлы сцен
│       └── states/           # Сохранённые состояния
└── main.py                   # Точка входа приложения
```

### API Endpoints
- `GET /api/game/start` - Начало новой игры
- `POST /api/game/action` - Выполнение действия
- `GET /api/game/state` - Получение текущего состояния
- `POST /api/game/save` - Сохранение игры
- `GET /api/game/load` - Загрузка сохранения

## Frontend (React)
### Компоненты
- Одностраничное приложение (SPA)
- Управление состоянием через React Context
- Адаптивный дизайн
- Анимации переходов

### Структура
```
frontend/
├── src/
│   ├── components/
│   │   ├── Game/
│   │   │   ├── Scene.jsx       # Отображение сцены
│   │   │   ├── Inventory.jsx   # Инвентарь
│   │   │   ├── Health.jsx      # Индикатор здоровья
│   │   │   └── Choices.jsx     # Варианты действий
│   │   ├── UI/
│   │   │   ├── Button.jsx      # Кнопки
│   │   │   ├── Dialog.jsx      # Диалоговые окна
│   │   │   └── Icons.jsx       # Иконки
│   │   └── Layout/
│   │       └── GameLayout.jsx  # Общий макет
│   ├── context/
│   │   └── GameContext.jsx     # Контекст игры
│   ├── hooks/
│   │   └── useGame.js          # Хук игровой логики
│   ├── services/
│   │   └── api.js              # Взаимодействие с API
│   └── App.jsx                 # Корневой компонент
└── index.html                  # Точка входа
```

## Формат данных

### Состояние игры
```json
{
  "player": {
    "name": "string",
    "health": 100,
    "inventory": ["item_id1", "item_id2"]
  },
  "current_scene": "scene_id",
  "visited_scenes": ["scene_id1", "scene_id2"],
  "game_flags": {
    "has_key": true,
    "talked_to_merchant": false
  }
}
```

### Формат сцены
```json
{
  "id": "scene_id",
  "description": "Описание сцены",
  "choices": [
    {
      "text": "Текст выбора",
      "requirements": {
        "item": "required_item",
        "health": 50
      },
      "effects": {
        "health": -10,
        "items": {
          "add": ["item_id"],
          "remove": ["used_item"]
        },
        "next_scene": "next_scene_id"
      }
    }
  ]
}
```

### Формат предмета
```json
{
  "id": "item_id",
  "name": "Название предмета",
  "description": "Описание предмета",
  "usable": true,
  "effect": {
    "type": "health",
    "value": 20
  }
}
```

## Взаимодействие компонентов
1. Frontend отправляет запросы к Backend API
2. Backend обрабатывает запросы и обновляет состояние игры
3. Состояние хранится в файловой системе в формате JSON
4. Frontend получает обновленное состояние и отображает изменения

## Сохранение прогресса
- Сохранения хранятся в JSON файлах в директории states/
- Каждое сохранение включает полное состояние игры
- Автосохранение после каждого значимого действия
