# Путешествие Героя - Текстовый Квест

Интерактивная текстовая игра-приключение, разработанная с использованием FastAPI и React.

## Технологии

### Backend
- Python 3.8+
- FastAPI
- Uvicorn

### Frontend
- React 18
- TypeScript
- Material-UI
- Vite

## Установка

### Backend

```bash
# Установка зависимостей Python
pip install -r requirements.txt

# Запуск сервера
python -m uvicorn backend.main:app --reload
```

### Frontend

```bash
# Переход в директорию frontend
cd frontend

# Установка зависимостей Node.js
npm install

# Запуск сервера разработки
npm run dev
```

## Игровой процесс

- Исследуйте загадочный замок
- Собирайте и используйте предметы
- Принимайте решения, влияющие на сюжет
- Следите за уровнем здоровья
- Сохраняйте и загружайте игру

## Структура проекта

```
pet1/
├── backend/
│   ├── app/
│   │   └── game.py
│   ├── data/
│   │   ├── items.py
│   │   └── scenes.py
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.tsx
│   │   └── main.tsx
│   └── package.json
└── requirements.txt
```

## Лицензия

MIT