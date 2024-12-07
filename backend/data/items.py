"""
Файл содержит все игровые предметы и их свойства
"""

ITEMS = {
    "old_key": {
        "id": "old_key",
        "name": "Старый ключ",
        "description": "Ржавый железный ключ. Возможно, он от какой-то двери в замке.",
        "usable": True,
        "effect": {
            "type": "story",
            "value": None
        }
    },
    "healing_potion": {
        "id": "healing_potion",
        "name": "Лечебное зелье",
        "description": "Красная жидкость в небольшом флаконе. Восстанавливает здоровье.",
        "usable": True,
        "effect": {
            "type": "health",
            "value": 30
        }
    },
    "sword": {
        "id": "sword",
        "name": "Старый меч",
        "description": "Потрёпанный, но всё ещё острый меч.",
        "usable": True,
        "effect": {
            "type": "combat",
            "value": 15
        }
    }
}
