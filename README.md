# Pathfinding Visualization with Pygame
![PathfindingVisualization](screenshots/pathfindingVisualization.png)

## Overview 

This Python program visualizes pathfinding algorithms (currently supports BFS) using Pygame. It allows users to interactively set start points, target points, and draw obstacles on a grid.

## Features
- **Interactive UI:** Set start, target points, and draw obstacles on a grid.
- **Adjustable Parameters:** Customize grid size, colors, and animation speed.
- **Real-Time Visualization:** Observe the pathfinding algorithm in action.


## Requirements

- Python 3.x
- Pygame library (`pip install pygame`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tymoteuszmilek/path-finding-visualization.git
   cd pathfinding-visualization/src
   ```

2. **Install the required dependencies:**
     
      ```bash
      pip install -r requirements.txt
      ```

## Usage
1. **Run the program:**
   
      ```bash
      python main.py
      ```
      
2. **Instructions**
  - **Draw walls** Hold left-click and drag to create obstacles.
  - **Set start position** Right-click on the desired starting point.
  - **Set target position** Right-click on the desired target destination.
  - **Start algorithm** Press any key to initiate the pathfinding process.
