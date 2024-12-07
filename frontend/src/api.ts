import axios from 'axios';
import { GameState } from './types';
import { API_URL } from './config';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const startNewGame = async (sessionId: string): Promise<GameState> => {
  const response = await api.post('/new-game', { session_id: sessionId });
  return response.data;
};

export const makeChoice = async (sessionId: string, choiceIndex: number): Promise<GameState> => {
  const response = await api.post('/make-choice', {
    session_id: sessionId,
    choice_index: choiceIndex,
  });
  return response.data;
};

export const useItem = async (sessionId: string, itemIndex: number): Promise<GameState> => {
  const response = await api.post('/use-item', {
    session_id: sessionId,
    item_index: itemIndex,
  });
  return response.data;
};

export const getGameState = async (sessionId: string): Promise<GameState> => {
  const response = await api.get(`/game-state/${sessionId}`);
  return response.data;
};

export const saveGame = async (sessionId: string): Promise<any> => {
  const response = await api.post(`/save-game/${sessionId}`);
  return response.data;
};

export const loadGame = async (sessionId: string, saveData: any): Promise<GameState> => {
  const response = await api.post(`/load-game/${sessionId}`, saveData);
  return response.data;
};
