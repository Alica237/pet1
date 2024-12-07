export interface Item {
  id: string;
  name: string;
  description: string;
  usable: boolean;
  effect?: {
    type: string;
    value: number;
  };
}

export interface Choice {
  text: string;
  next_scene: string;
  effects: {
    health?: number;
    science_points?: number;
    items?: string[];
  };
}

export interface Scene {
  id: string;
  description: string;
  choices: Choice[];
}

export interface GameState {
  health: number;
  science_points: number;
  inventory: Item[];
  current_scene: Scene;
  game_over: boolean;
  ending?: string;
}
