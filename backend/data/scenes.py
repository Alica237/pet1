"""
Файл содержит все игровые сцены и их взаимосвязи
"""

SCENES = {
    "start": {
        "id": "start",
        "description": """
        Вы стоите перед древним замком. Его мрачные стены возвышаются над вами, 
        а массивные ворота слегка приоткрыты. Холодный ветер доносит странные звуки изнутри.
        """,
        "choices": [
            {
                "text": "Войти в замок",
                "next_scene": "castle_hall",
                "effects": {"health": 0}
            },
            {
                "text": "Осмотреть окрестности",
                "next_scene": "castle_surroundings",
                "effects": {"health": 0}
            }
        ]
    },
    "castle_hall": {
        "id": "castle_hall",
        "description": """
        Вы находитесь в главном зале замка. Пыльные гобелены украшают стены, 
        а в центре зала стоит старинный рыцарский доспех. На полу вы замечаете следы.
        """,
        "choices": [
            {
                "text": "Осмотреть доспех",
                "next_scene": "examine_armor",
                "effects": {"health": 0, "items": ["old_key"]}
            },
            {
                "text": "Подняться по лестнице",
                "next_scene": "upper_floor",
                "effects": {"health": 0}
            }
        ]
    },
    "castle_surroundings": {
        "id": "castle_surroundings",
        "description": """
        Обходя замок, вы находите небольшой сад. Среди зарослей виднеется старый колодец,
        а рядом лежит какой-то предмет.
        """,
        "choices": [
            {
                "text": "Подойти к колодцу",
                "next_scene": "well",
                "effects": {"health": 0}
            },
            {
                "text": "Поднять предмет",
                "next_scene": "pick_item",
                "effects": {"health": 0, "items": ["healing_potion"]}
            }
        ]
    }
}
