"""
Файл содержит все игровые сцены научно-фантастического квеста
"""

SCENES = {
    "start": {
        "id": "start",
        "description": """
        Вы находитесь в научной лаборатории станции "Гагарин" на орбите экзопланеты Kepler-442b.
        Ваши приборы только что зарегистрировали странный сигнал с поверхности планеты.
        Мониторы показывают необычные энергетические колебания.
        """,
        "choices": [
            {
                "text": "Немедленно доложить руководству",
                "next_scene": "report_to_command",
                "effects": {
                    "health": 0,
                    "science_points": 1,
                    "items": []
                }
            },
            {
                "text": "Провести предварительный анализ данных",
                "next_scene": "analyze_signal",
                "effects": {
                    "health": 0,
                    "science_points": 5,
                    "items": ["initial_data"]
                }
            },
            {
                "text": "Проверить защитные системы станции",
                "next_scene": "check_defenses",
                "effects": {
                    "health": 5,
                    "science_points": 0,
                    "items": ["shield_report"]
                }
            }
        ]
    },

    # Путь безопасности
    "check_defenses": {
        "id": "check_defenses",
        "description": """
        Системы защиты станции работают в штатном режиме, но сигнал вызывает небольшие помехи.
        Сканеры дальнего действия показывают увеличение энергетических колебаний на поверхности.
        """,
        "choices": [
            {
                "text": "Усилить защитные поля станции",
                "next_scene": "enhance_shields",
                "effects": {
                    "health": 10,
                    "science_points": 2,
                    "items": ["shield_generator"]
                }
            },
            {
                "text": "Подготовить спасательные капсулы",
                "next_scene": "prepare_escape_pods",
                "effects": {
                    "health": 15,
                    "science_points": 0,
                    "items": ["emergency_kit"]
                }
            },
            {
                "text": "Запустить дроны наблюдения",
                "next_scene": "launch_drones",
                "effects": {
                    "health": 0,
                    "science_points": 5,
                    "items": ["drone_data"]
                }
            }
        ]
    },

    "enhance_shields": {
        "id": "enhance_shields",
        "description": """
        Защитные поля станции работают на повышенной мощности. Это дает вам время для более
        детального изучения ситуации. Энергетические колебания на планете усиливаются.
        """,
        "choices": [
            {
                "text": "Создать мобильный щит для высадки",
                "next_scene": "create_mobile_shield",
                "effects": {
                    "health": 20,
                    "science_points": 5,
                    "items": ["portable_shield"]
                }
            },
            {
                "text": "Провести анализ колебаний",
                "next_scene": "analyze_signal",
                "effects": {
                    "health": 0,
                    "science_points": 8,
                    "items": ["signal_analysis"]
                }
            },
            {
                "text": "Эвакуировать станцию",
                "next_scene": "evacuation_ending",
                "effects": {
                    "health": 10,
                    "science_points": -5,
                    "items": []
                }
            }
        ]
    },

    # Путь инженера
    "engineering_approach": {
        "id": "engineering_approach",
        "description": """
        Вы решаете подойти к проблеме с инженерной точки зрения. Ваша команда начинает
        подготовку оборудования для создания исследовательской базы на поверхности.
        """,
        "choices": [
            {
                "text": "Развернуть автоматизированную базу",
                "next_scene": "deploy_auto_base",
                "effects": {
                    "health": 5,
                    "science_points": 8,
                    "items": ["base_controls"]
                }
            },
            {
                "text": "Создать сеть сенсоров",
                "next_scene": "sensor_network",
                "effects": {
                    "health": 0,
                    "science_points": 12,
                    "items": ["sensor_data"]
                }
            },
            {
                "text": "Построить защищенный бункер",
                "next_scene": "build_bunker",
                "effects": {
                    "health": 15,
                    "science_points": 5,
                    "items": ["bunker_key"]
                }
            }
        ]
    },

    "deploy_auto_base": {
        "id": "deploy_auto_base",
        "description": """
        Автоматизированная база успешно развернута. Роботы-строители начинают возводить
        основные структуры. Сканеры базы регистрируют странные подземные активности.
        """,
        "choices": [
            {
                "text": "Расширить сеть сенсоров",
                "next_scene": "expand_sensors",
                "effects": {
                    "health": 0,
                    "science_points": 15,
                    "items": ["advanced_sensors"]
                }
            },
            {
                "text": "Укрепить фундамент базы",
                "next_scene": "reinforce_base",
                "effects": {
                    "health": 10,
                    "science_points": 8,
                    "items": ["reinforced_structures"]
                }
            },
            {
                "text": "Начать подземное бурение",
                "next_scene": "start_drilling",
                "effects": {
                    "health": -5,
                    "science_points": 20,
                    "items": ["drill_samples"]
                }
            }
        ]
    },

    # Новые сцены для путей
    "report_to_command": {
        "id": "report_to_command",
        "description": """
        Вы отправляете срочный отчет командованию. Они приказывают продолжить наблюдение
        и собрать больше данных перед принятием дальнейших решений.
        """,
        "choices": [
            {
                "text": "Проверить защитные системы",
                "next_scene": "check_defenses",
                "effects": {
                    "health": 5,
                    "science_points": 2,
                    "items": ["shield_report"]
                }
            },
            {
                "text": "Начать инженерный анализ",
                "next_scene": "engineering_approach",
                "effects": {
                    "health": 0,
                    "science_points": 5,
                    "items": []
                }
            }
        ]
    },

    "analyze_signal": {
        "id": "analyze_signal",
        "description": """
        Предварительный анализ показывает, что сигнал имеет искусственное происхождение.
        Его структура указывает на высокоразвитую технологическую цивилизацию.
        """,
        "choices": [
            {
                "text": "Начать инженерное исследование",
                "next_scene": "engineering_approach",
                "effects": {
                    "health": 0,
                    "science_points": 10,
                    "items": ["signal_analysis"]
                }
            },
            {
                "text": "Усилить защиту станции",
                "next_scene": "enhance_shields",
                "effects": {
                    "health": 10,
                    "science_points": 5,
                    "items": []
                }
            }
        ]
    },

    "launch_drones": {
        "id": "launch_drones",
        "description": """
        Разведывательные дроны запущены и передают данные. Они обнаруживают странные
        структуры на поверхности планеты, похожие на древние руины.
        """,
        "choices": [
            {
                "text": "Начать инженерное исследование",
                "next_scene": "engineering_approach",
                "effects": {
                    "health": 0,
                    "science_points": 15,
                    "items": ["drone_data"]
                }
            },
            {
                "text": "Укрепить оборону",
                "next_scene": "enhance_shields",
                "effects": {
                    "health": 10,
                    "science_points": 5,
                    "items": []
                }
            }
        ]
    },

    "prepare_escape_pods": {
        "id": "prepare_escape_pods",
        "description": """
        Спасательные капсулы готовы к эвакуации. Экипаж находится в состоянии повышенной
        готовности. Сигнал с планеты становится сильнее.
        """,
        "choices": [
            {
                "text": "Эвакуировать станцию",
                "next_scene": "evacuation_ending",
                "effects": {
                    "health": 20,
                    "science_points": -10,
                    "items": ["emergency_kit"]
                }
            },
            {
                "text": "Продолжить исследование",
                "next_scene": "engineering_approach",
                "effects": {
                    "health": -5,
                    "science_points": 15,
                    "items": []
                }
            }
        ]
    },

    "create_mobile_shield": {
        "id": "create_mobile_shield",
        "description": """
        Мобильный щит успешно создан. Это позволит безопасно исследовать поверхность
        планеты, защищаясь от неизвестных угроз.
        """,
        "choices": [
            {
                "text": "Начать исследование поверхности",
                "next_scene": "engineering_approach",
                "effects": {
                    "health": 15,
                    "science_points": 10,
                    "items": ["portable_shield"]
                }
            },
            {
                "text": "Подготовить эвакуацию",
                "next_scene": "prepare_escape_pods",
                "effects": {
                    "health": 10,
                    "science_points": 0,
                    "items": []
                }
            }
        ]
    },

    "sensor_network": {
        "id": "sensor_network",
        "description": """
        Сеть сенсоров развернута и собирает данные. Показания указывают на масштабную
        подземную активность неизвестного происхождения.
        """,
        "choices": [
            {
                "text": "Расширить сеть сенсоров",
                "next_scene": "expand_sensors",
                "effects": {
                    "health": 0,
                    "science_points": 20,
                    "items": ["advanced_sensors"]
                }
            },
            {
                "text": "Начать бурение без подготовки",
                "next_scene": "death_collapse",
                "effects": {
                    "health": -100,
                    "science_points": 0,
                    "items": []
                }
            },
            {
                "text": "Начать бурение с предосторожностями",
                "next_scene": "start_drilling",
                "effects": {
                    "health": -5,
                    "science_points": 25,
                    "items": []
                }
            }
        ]
    },

    "build_bunker": {
        "id": "build_bunker",
        "description": """
        Защищенный исследовательский бункер построен. Он обеспечит безопасное место для
        изучения находок и защиту от возможных угроз.
        """,
        "choices": [
            {
                "text": "Расширить исследования",
                "next_scene": "sensor_network",
                "effects": {
                    "health": 10,
                    "science_points": 15,
                    "items": ["bunker_key"]
                }
            },
            {
                "text": "Укрепить оборону",
                "next_scene": "reinforce_base",
                "effects": {
                    "health": 20,
                    "science_points": 5,
                    "items": []
                }
            }
        ]
    },

    "reinforce_base": {
        "id": "reinforce_base",
        "description": """
        База успешно укреплена. Новые защитные сооружения значительно повышают безопасность
        персонала и оборудования.
        """,
        "choices": [
            {
                "text": "Продолжить исследования",
                "next_scene": "start_drilling",
                "effects": {
                    "health": 15,
                    "science_points": 10,
                    "items": ["reinforced_structures"]
                }
            },
            {
                "text": "Расширить сеть сенсоров",
                "next_scene": "expand_sensors",
                "effects": {
                    "health": 5,
                    "science_points": 20,
                    "items": []
                }
            }
        ]
    },

    "expand_sensors": {
        "id": "expand_sensors",
        "description": """
        Расширенная сеть сенсоров показывает детальную картину подземной активности.
        Обнаружены признаки древней технологической цивилизации.
        """,
        "choices": [
            {
                "text": "Начать раскопки",
                "next_scene": "start_drilling",
                "effects": {
                    "health": -5,
                    "science_points": 30,
                    "items": ["advanced_sensors"]
                }
            },
            {
                "text": "Укрепить базу",
                "next_scene": "reinforce_base",
                "effects": {
                    "health": 15,
                    "science_points": 10,
                    "items": []
                }
            }
        ]
    },

    "start_drilling": {
        "id": "start_drilling",
        "description": """
        Бурение началось. На глубине 100 метров обнаружен вход в древний комплекс.
        Датчики показывают наличие энергетической активности внутри.
        """,
        "choices": [
            {
                "text": "Исследовать комплекс без защиты",
                "next_scene": "death_radiation",
                "effects": {
                    "health": -100,
                    "science_points": 0,
                    "items": []
                }
            },
            {
                "text": "Исследовать комплекс в защитном костюме",
                "next_scene": "engineering_victory",
                "effects": {
                    "health": -10,
                    "science_points": 40,
                    "items": ["drill_samples"]
                }
            },
            {
                "text": "Отступить и укрепить оборону",
                "next_scene": "evacuation_ending",
                "effects": {
                    "health": 10,
                    "science_points": 15,
                    "items": []
                }
            }
        ]
    },

    # Сцены смерти
    "death_radiation": {
        "id": "death_radiation",
        "description": """
        Войдя в древний комплекс без защитного костюма, вы подвергаетесь смертельной дозе
        неизвестного излучения. Последнее, что вы видите - странное свечение вокруг...
        КОНЕЦ ИГРЫ - Фатальная ошибка
        """,
        "choices": []
    },

    "death_collapse": {
        "id": "death_collapse",
        "description": """
        Начав бурение без proper подготовки и укрепления стен, вы вызываете обрушение
        подземной полости. Спастись не удается...
        КОНЕЦ ИГРЫ - Фатальная ошибка
        """,
        "choices": []
    },

    # Концовки
    "evacuation_ending": {
        "id": "evacuation_ending",
        "description": """
        Вы принимаете решение об эвакуации станции. Это безопасный, но консервативный выбор.
        Тайна сигнала остается неразгаданной, но весь экипаж в безопасности.
        КОНЕЦ ИГРЫ - Путь безопасности
        """,
        "choices": []
    },

    "engineering_victory": {
        "id": "engineering_victory",
        "description": """
        Исследование древнего комплекса привело к невероятному открытию. Вы нашли
        технологии древней цивилизации, которые изменят будущее человечества.
        КОНЕЦ ИГРЫ - Инженерная победа
        """,
        "choices": []
    }
}

# Константы для игровой механики
MINIMUM_HEALTH = 0
MAXIMUM_HEALTH = 100
MINIMUM_SCIENCE = 0
MAXIMUM_SCIENCE = 100

# Условия для концовок
EVACUATION_MIN_HEALTH = 60
SCIENCE_VICTORY_MIN_SCIENCE = 80
ENGINEERING_VICTORY_MIN_SCIENCE = 60
ENGINEERING_VICTORY_MIN_HEALTH = 40

# Определение концовок
ENDINGS = {
    "evacuation": {
        "description": """
        Вы приняли решение об эвакуации. Несмотря на неполные данные,
        ваше здоровье и безопасность команды остались в приоритете.
        Это не полный провал, но и не победа. Возможно, следующая экспедиция
        будет более успешной.
        """,
        "title": "Эвакуация - Частичный успех",
        "required_science_points": 30,
        "min_health": EVACUATION_MIN_HEALTH,
        "required_items": []
    },
    "science_victory": {
        "description": """
        Благодаря вашему научному подходу, удалось раскрыть тайны древней
        цивилизации Kepler-442b. Ваши исследования войдут в историю
        и откроют новую главу в развитии человечества.
        """,
        "title": "Научный прорыв - Полная победа",
        "required_science_points": SCIENCE_VICTORY_MIN_SCIENCE,
        "min_health": 40,
        "required_items": ["quantum_analyzer", "alien_data"]
    },
    "engineering_victory": {
        "description": """
        Ваши инженерные решения позволили установить контакт с древними
        технологиями. Это огромный шаг вперед в развитии человеческой
        цивилизации.
        """,
        "title": "Инженерный успех - Полная победа",
        "required_science_points": ENGINEERING_VICTORY_MIN_SCIENCE,
        "min_health": ENGINEERING_VICTORY_MIN_HEALTH,
        "required_items": ["shield_generator", "base_control"]
    },
    "death": {
        "description": """
        К сожалению, рискованные решения привели к фатальным последствиям.
        Следующая экспедиция учтет ваш опыт и будет действовать осторожнее.
        """,
        "title": "Миссия провалена",
        "required_science_points": 0,
        "min_health": 0,
        "required_items": []
    }
}
