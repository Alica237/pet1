import React, { useEffect, useState } from 'react';
import { Container, Box, Typography, LinearProgress } from '@mui/material';
import { v4 as uuidv4 } from 'uuid';
import Scene from './components/Scene';
import Inventory from './components/Inventory';
import { GameState } from './types';
import * as api from './api';

const App: React.FC = () => {
  const [sessionId] = useState(() => uuidv4());
  const [gameState, setGameState] = useState<GameState | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initGame = async () => {
      try {
        const state = await api.startNewGame(sessionId);
        setGameState(state);
      } catch (error) {
        console.error('Failed to start game:', error);
      } finally {
        setLoading(false);
      }
    };

    initGame();
  }, [sessionId]);

  const handleChoice = async (choiceIndex: number) => {
    if (!gameState) return;
    
    setLoading(true);
    try {
      const newState = await api.makeChoice(sessionId, choiceIndex);
      setGameState(newState);
    } catch (error) {
      console.error('Failed to make choice:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleUseItem = async (itemIndex: number) => {
    if (!gameState) return;
    
    setLoading(true);
    try {
      const newState = await api.useItem(sessionId, itemIndex);
      setGameState(newState);
    } catch (error) {
      console.error('Failed to use item:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading && !gameState) {
    return (
      <Container>
        <Box sx={{ width: '100%', mt: 4 }}>
          <LinearProgress />
        </Box>
      </Container>
    );
  }

  if (!gameState) {
    return (
      <Container>
        <Typography color="error">
          Failed to load game. Please refresh the page.
        </Typography>
      </Container>
    );
  }

  return (
    <Container>
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom align="center">
          Путешествие Героя
        </Typography>
        
        <Box sx={{ display: 'flex', gap: 2, my: 3 }}>
          <Typography variant="h6">
            Здоровье: {gameState.health}
          </Typography>
        </Box>

        <Box sx={{ display: 'flex', gap: 4 }}>
          <Box sx={{ flex: 1 }}>
            <Scene 
              scene={gameState.current_scene} 
              onChoice={handleChoice}
            />
          </Box>
          
          <Box sx={{ width: 300 }}>
            <Inventory 
              items={gameState.inventory.map(item => item.name)}
              onUseItem={handleUseItem}
            />
          </Box>
        </Box>

        {gameState.game_over && (
          <Typography variant="h5" color="error" align="center" sx={{ mt: 4 }}>
            Игра окончена
          </Typography>
        )}
      </Box>
    </Container>
  );
};

export default App;
