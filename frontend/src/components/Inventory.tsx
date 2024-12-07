import React from 'react';
import { 
  Box, 
  Typography, 
  List, 
  ListItem, 
  ListItemText, 
  ListItemSecondaryAction,
  IconButton,
  Divider,
  Tooltip
} from '@mui/material';
import { 
  ArrowForward as UseItemIcon
} from '@mui/icons-material';

interface Item {
  name: string;
  description: string;
  usable: boolean;
}

interface InventoryProps {
  items: Item[];
  onUseItem: (index: number) => void;
  disabled: boolean;
}

const Inventory: React.FC<InventoryProps> = ({ items, onUseItem, disabled }) => {
  if (items.length === 0) {
    return (
      <Box sx={{ mt: 3 }}>
        <Typography variant="h6" gutterBottom>
          Инвентарь
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Инвентарь пуст
        </Typography>
      </Box>
    );
  }

  return (
    <Box sx={{ mt: 3 }}>
      <Typography variant="h6" gutterBottom>
        Инвентарь
      </Typography>
      <List>
        {items.map((item, index) => (
          <React.Fragment key={index}>
            <ListItem>
              <ListItemText
                primary={item.name}
                secondary={item.description}
              />
              {item.usable && (
                <ListItemSecondaryAction>
                  <Tooltip title="Использовать предмет">
                    <IconButton
                      edge="end"
                      onClick={() => onUseItem(index)}
                      disabled={disabled}
                    >
                      <UseItemIcon />
                    </IconButton>
                  </Tooltip>
                </ListItemSecondaryAction>
              )}
            </ListItem>
            {index < items.length - 1 && <Divider />}
          </React.Fragment>
        ))}
      </List>
    </Box>
  );
};

export default Inventory;
