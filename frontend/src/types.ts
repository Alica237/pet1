export interface Item {
  id: string;
  name: string;
  description: string;
  usable: boolean;
  effect: {
    type: string;
    value: number | null;
  };
}

export interface Scene {
  id: string;
  description: string;
  choices: Array<{
    text: string;
    next_scene: string;
    effects: {
      health?: number;
      items?: string[];
    };
  }>;
}

export interface GameState {
  health: number;
  inventory: Item[];
  current_scene: Scene;
  game_over: boolean;
}
