from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict
from backend.app.game import Game

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Разрешаем запросы только с фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Хранилище игровых сессий
games: Dict[str, Game] = {}

class GameSession(BaseModel):
    session_id: str

class GameChoice(BaseModel):
    session_id: str
    choice_index: int

class ItemUse(BaseModel):
    session_id: str
    item_index: int

@app.get("/")
async def root():
    """Проверка работоспособности API"""
    return {"message": "Text Quest API is running"}

@app.post("/new-game")
async def new_game(session: GameSession):
    """Создать новую игру"""
    games[session.session_id] = Game()
    return games[session.session_id].get_game_state()

@app.post("/make-choice")
async def make_choice(choice: GameChoice):
    """Сделать выбор в игре"""
    if choice.session_id not in games:
        raise HTTPException(status_code=404, detail="Игровая сессия не найдена")
    
    try:
        return games[choice.session_id].make_choice(choice.choice_index)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/use-item")
async def use_item(item: ItemUse):
    """Использовать предмет из инвентаря"""
    if item.session_id not in games:
        raise HTTPException(status_code=404, detail="Игровая сессия не найдена")
    
    try:
        return games[item.session_id].use_item(item.item_index)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/game-state/{session_id}")
async def get_game_state(session_id: str):
    """Получить текущее состояние игры"""
    if session_id not in games:
        raise HTTPException(status_code=404, detail="Игровая сессия не найдена")
    
    return games[session_id].get_game_state()

@app.post("/save-game/{session_id}")
async def save_game(session_id: str):
    """Сохранить игру"""
    if session_id not in games:
        raise HTTPException(status_code=404, detail="Игровая сессия не найдена")
    
    return games[session_id].save_game()

@app.post("/load-game/{session_id}")
async def load_game(session_id: str, save_data: dict):
    """Загрузить игру"""
    if session_id not in games:
        games[session_id] = Game()
    
    games[session_id].load_game(save_data)
    return games[session_id].get_game_state()
