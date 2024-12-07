import React from 'react';
import {
  Box,
  Typography,
  Button,
  Stack,
  Paper,
} from '@mui/material';
import { Scene as SceneType } from '../types';

interface SceneProps {
  scene: SceneType;
  onChoice: (index: number) => void;
}

const Scene: React.FC<SceneProps> = ({ scene, onChoice }) => {
  return (
    <Paper elevation={3} sx={{ p: 3, maxWidth: 600, mx: 'auto', my: 2 }}>
      <Typography variant="body1" paragraph>
        {scene.description}
      </Typography>
      
      <Stack spacing={2} sx={{ mt: 3 }}>
        {scene.choices.map((choice, index) => (
          <Button
            key={index}
            variant="contained"
            color="primary"
            onClick={() => onChoice(index)}
            fullWidth
          >
            {choice.text}
          </Button>
        ))}
      </Stack>
    </Paper>
  );
};

export default Scene;
