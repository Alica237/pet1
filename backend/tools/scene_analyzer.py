"""
Анализатор сцен для поиска несвязанных путей
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from backend.data.scenes import SCENES

def analyze_scenes():
    # Все сцены
    all_scenes = set(SCENES.keys())
    
    # Сцены, в которые можно попасть
    reachable_scenes = set()
    
    # Собираем все сцены, на которые есть ссылки
    for scene_id, scene in SCENES.items():
        for choice in scene["choices"]:
            next_scene = choice["next_scene"]
            reachable_scenes.add(next_scene)
    
    # Находим сцены без входящих ссылок
    unreachable = all_scenes - reachable_scenes - {"start"}  # Исключаем стартовую сцену
    if unreachable:
        print("Сцены без входящих ссылок:")
        for scene in unreachable:
            print(f"- {scene}")
    
    # Находим ссылки на несуществующие сцены
    referenced_scenes = set()
    for scene in SCENES.values():
        for choice in scene["choices"]:
            referenced_scenes.add(choice["next_scene"])
    
    missing_scenes = referenced_scenes - all_scenes
    if missing_scenes:
        print("\nСсылки на несуществующие сцены:")
        for scene in missing_scenes:
            print(f"- {scene}")
            # Показываем, где используются
            for scene_id, scene_data in SCENES.items():
                for choice in scene_data["choices"]:
                    if choice["next_scene"] in missing_scenes:
                        print(f"  Используется в сцене: {scene_id}")
    
    # Находим сцены без исходящих ссылок (кроме концовок)
    dead_ends = set()
    for scene_id, scene in SCENES.items():
        if not scene["choices"] and not scene_id.endswith("_ending") and not scene_id.endswith("_victory"):
            dead_ends.add(scene_id)
    
    if dead_ends:
        print("\nТупиковые сцены (без выборов и не концовки):")
        for scene in dead_ends:
            print(f"- {scene}")

if __name__ == "__main__":
    analyze_scenes()
