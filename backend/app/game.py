from typing import Dict, List, Optional
from backend.data.scenes import SCENES, MINIMUM_HEALTH, MAXIMUM_HEALTH, MINIMUM_SCIENCE, MAXIMUM_SCIENCE, ENDINGS
from backend.data.items import ITEMS

class Game:
    def __init__(self):
        self.health: int = 100
        self.science_points: int = 0
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
                effects = choice["effects"]
                # Изменение здоровья
                if "health" in effects:
                    self.change_health(effects["health"])
                
                # Изменение очков науки
                if "science_points" in effects:
                    self.change_science_points(effects["science_points"])
                
                # Добавление предметов
                if "items" in effects:
                    for item_id in effects["items"]:
                        self.add_item(item_id)
            
            # Переход к следующей сцене
            self.current_scene = choice["next_scene"]
            return self.get_game_state()
        
        raise ValueError("Недопустимый индекс выбора")
    
    def change_health(self, amount: int) -> None:
        """Изменить здоровье игрока"""
        self.health = max(MINIMUM_HEALTH, min(MAXIMUM_HEALTH, self.health + amount))
    
    def change_science_points(self, amount: int) -> None:
        """Изменить очки науки"""
        self.science_points = max(MINIMUM_SCIENCE, min(MAXIMUM_SCIENCE, self.science_points + amount))
    
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
                elif effect["type"] == "science":
                    self.change_science_points(effect["value"])
                
                # Удаляем использованный предмет
                self.inventory.pop(item_index)
                
            return self.get_game_state()
        
        raise ValueError("Недопустимый индекс предмета")
    
    def check_ending(self) -> Optional[str]:
        """Проверить достижение одной из концовок"""
        for ending_id, requirements in ENDINGS.items():
            if (self.science_points >= requirements["required_science_points"] and
                self.health >= requirements["min_health"] and
                all(item in self.inventory for item in requirements["required_items"])):
                return ending_id
        return None
    
    def get_game_state(self) -> dict:
        """Получить текущее состояние игры"""
        ending = self.check_ending()
        return {
            "health": self.health,
            "science_points": self.science_points,
            "inventory": [ITEMS[item_id] for item_id in self.inventory],
            "current_scene": self.get_current_scene(),
            "game_over": self.health <= 0,
            "ending": ending
        }
    
    def save_game(self) -> dict:
        """Сохранить игру"""
        return {
            "health": self.health,
            "science_points": self.science_points,
            "inventory": self.inventory,
            "current_scene": self.current_scene,
            "game_flags": self.game_flags
        }
    
    def load_game(self, save_data: dict) -> None:
        """Загрузить игру"""
        self.health = save_data["health"]
        self.science_points = save_data.get("science_points", 0)  # Для совместимости со старыми сохранениями
        self.inventory = save_data["inventory"]
        self.current_scene = save_data["current_scene"]
        self.game_flags = save_data["game_flags"]
