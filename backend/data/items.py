"""
Файл содержит все игровые предметы и их свойства
"""

ITEMS = {
    # Научные предметы
    "initial_data": {
        "id": "initial_data",
        "name": "Начальные данные",
        "description": "Первичный анализ странного сигнала с планеты.",
        "usable": True,
        "effect": {
            "type": "science",
            "value": 2
        }
    },
    "signal_analysis": {
        "id": "signal_analysis",
        "name": "Анализ сигнала",
        "description": "Подробный спектральный анализ сигнала с планеты.",
        "usable": True,
        "effect": {
            "type": "science",
            "value": 8
        }
    },
    "quantum_analyzer": {
        "id": "quantum_analyzer",
        "name": "Квантовый анализатор",
        "description": "Продвинутый прибор для изучения квантовых явлений.",
        "usable": True,
        "effect": {
            "type": "science",
            "value": 10
        }
    },

    # Предметы для пути безопасности
    "shield_report": {
        "id": "shield_report",
        "name": "Отчет о защите",
        "description": "Данные о состоянии защитных систем станции.",
        "usable": True,
        "effect": {
            "type": "science",
            "value": 3
        }
    },
    "shield_generator": {
        "id": "shield_generator",
        "name": "Генератор щита",
        "description": "Создает защитное поле вокруг пользователя.",
        "usable": True,
        "effect": {
            "type": "health",
            "value": 20
        }
    },
    "emergency_kit": {
        "id": "emergency_kit",
        "name": "Аварийный комплект",
        "description": "Набор для выживания в экстренных ситуациях.",
        "usable": True,
        "effect": {
            "type": "health",
            "value": 30
        }
    },
    "portable_shield": {
        "id": "portable_shield",
        "name": "Портативный щит",
        "description": "Мобильное защитное устройство для исследований.",
        "usable": True,
        "effect": {
            "type": "health",
            "value": 15
        }
    },
    "drone_data": {
        "id": "drone_data",
        "name": "Данные дронов",
        "description": "Информация, собранная разведывательными дронами.",
        "usable": True,
        "effect": {
            "type": "science",
            "value": 6
        }
    },

    # Предметы для пути инженера
    "base_controls": {
        "id": "base_controls",
        "name": "Пульт управления базой",
        "description": "Система управления автоматизированной базой.",
        "usable": True,
        "effect": {
            "type": "science",
            "value": 8
        }
    },
    "sensor_data": {
        "id": "sensor_data",
        "name": "Данные сенсоров",
        "description": "Показания сети научных сенсоров.",
        "usable": True,
        "effect": {
            "type": "science",
            "value": 10
        }
    },
    "bunker_key": {
        "id": "bunker_key",
        "name": "Ключ от бункера",
        "description": "Доступ к защищенному исследовательскому бункеру.",
        "usable": True,
        "effect": {
            "type": "health",
            "value": 10
        }
    },
    "advanced_sensors": {
        "id": "advanced_sensors",
        "name": "Продвинутые сенсоры",
        "description": "Улучшенная система сбора данных.",
        "usable": True,
        "effect": {
            "type": "science",
            "value": 15
        }
    },
    "reinforced_structures": {
        "id": "reinforced_structures",
        "name": "Укрепленные конструкции",
        "description": "Усиленные защитные сооружения базы.",
        "usable": True,
        "effect": {
            "type": "health",
            "value": 25
        }
    },
    "drill_samples": {
        "id": "drill_samples",
        "name": "Образцы бурения",
        "description": "Геологические образцы с большой глубины.",
        "usable": True,
        "effect": {
            "type": "science",
            "value": 20
        }
    }
}
