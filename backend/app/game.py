from typing import Dict, List, Optional
from backend.data.scenes import SCENES
from backend.data.items import ITEMS

class Game:
    def __init__(self):
        self.health: int = 100
        self.inventory: List[str] = []
        self.current_scene: str = "start"
        self.game_flags: Dict[str, bool] = {}
        
    def get_current_scene(self) -> dict:
        """Получить текущую сцену"""
        return SCENES[self.current_scene]
    
    def make_choice(self, choice_index: int) -> dict:
        """Сделать выбор в текущей сцене"""
        scene = self.get_current_scene()
        if 0 <= choice_index < len(scene["choices"]):
            choice = scene["choices"][choice_index]
            
            # Применяем эффекты выбора
            if "effects" in choice:
                # Изменение здоровья
                if "health" in choice["effects"]:
                    self.change_health(choice["effects"]["health"])
                
                # Добавление предметов
                if "items" in choice["effects"]:
                    for item_id in choice["effects"]["items"]:
                        self.add_item(item_id)
            
            # Переход к следующей сцене
            self.current_scene = choice["next_scene"]
            return self.get_game_state()
        
        raise ValueError("Недопустимый индекс выбора")
    
    def change_health(self, amount: int) -> None:
        """Изменить здоровье игрока"""
        self.health = max(0, min(100, self.health + amount))
    
    def add_item(self, item_id: str) -> None:
        """Добавить предмет в инвентарь"""
        if len(self.inventory) < 10:  # Максимум 10 предметов
            self.inventory.append(item_id)
    
    def use_item(self, item_index: int) -> dict:
        """Использовать предмет из инвентаря"""
        if 0 <= item_index < len(self.inventory):
            item_id = self.inventory[item_index]
            item = ITEMS[item_id]
            
            if item["usable"]:
                effect = item["effect"]
                if effect["type"] == "health":
                    self.change_health(effect["value"])
                
                # Удаляем использованный предмет
                self.inventory.pop(item_index)
                
            return self.get_game_state()
        
        raise ValueError("Недопустимый индекс предмета")
    
    def get_game_state(self) -> dict:
        """Получить текущее состояние игры"""
        return {
            "health": self.health,
            "inventory": [ITEMS[item_id] for item_id in self.inventory],
            "current_scene": self.get_current_scene(),
            "game_over": self.health <= 0
        }
    
    def save_game(self) -> dict:
        """Сохранить игру"""
        return {
            "health": self.health,
            "inventory": self.inventory,
            "current_scene": self.current_scene,
            "game_flags": self.game_flags
        }
    
    def load_game(self, save_data: dict) -> None:
        """Загрузить игру"""
        self.health = save_data["health"]
        self.inventory = save_data["inventory"]
        self.current_scene = save_data["current_scene"]
        self.game_flags = save_data["game_flags"]
