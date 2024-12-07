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
  disabled: boolean;
}

const Scene: React.FC<SceneProps> = ({ scene, onChoice, disabled }) => {
  return (
    <Paper elevation={3} sx={{ p: 3, maxWidth: 600, mx: 'auto', my: 2 }}>
      <Typography variant="body1" paragraph sx={{ mb: 3, whiteSpace: 'pre-line' }}>
        {scene.description}
      </Typography>
      
      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1, mt: 3 }}>
        {scene.choices.map((choice, index) => (
          <Button
            key={index}
            variant="contained"
            color="primary"
            onClick={() => onChoice(index)}
            disabled={disabled}
            sx={{
              textTransform: 'none',
              justifyContent: 'flex-start',
              padding: '12px 20px',
              lineHeight: 1.3
            }}
          >
            {choice.text}
          </Button>
        ))}
      </Box>
    </Paper>
  );
};

export default Scene;
