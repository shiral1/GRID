# GRID
You cannot control the agent. You can only shape the world. Minimize cost
  
  
## Core Idea

- The grid defines movement cost.
- The agent minimizes cumulative cost.
- The player can place a limited number of tiles.
- Press RUN to execute the computed path.

## Rules

- Movement is 4-directional.
- Empty tiles cost 1.
- Slow tiles cost 5.
- Walls are impassable.
- Hazards cause failure (or: hazards have high cost).
- The agent uses A* search with Manhattan distance.

## Controls

Left Click      – Place tile  
Right Click     – Remove tile  
1 | 2 | 3       – Switch tile type  
SPACE / ENTER   – Run pathfinding  
R               – Reset level  

## Technical Overview

- Grid stored as 2D list.
- A* implemented with priority queue.
- Levels loaded from text files.
- Path cost computed as sum of tile weights.