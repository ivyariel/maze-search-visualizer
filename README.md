# 🔍 Advanced Search Algorithm Explorer

An interactive Graphical User Interface (GUI) built with Python and Tkinter for visualizing and comparing five classic search algorithms on a custom maze.

## ✨ Key Features

- **Supports 5 Search Algorithms**:
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - Uniform-Cost Search (UCS)
  - Greedy Best-First Search
  - A* Search (A Star)
- **Modern UI Design**: Dark gradient background with neon-style accents. Flat, button-like selection cards provide clear visual feedback.
- **One-Click Execution**: Select an algorithm and hit "START SEARCH" to run the logic immediately.
- **Keyboard Shortcuts**: Use number keys `1` to `5` to quickly switch algorithms, and press `Enter` to start the search.
- **Real-time Status**: The bottom label updates instantly to show your currently selected algorithm.
- **JSON-based Maze Configuration**: Easily change the maze layout, start point, and goals by editing the `maze2.json` file.


## 🎮 Usage Guide

After launching the program, the dark‑themed selection interface will appear.

### Select an Algorithm

**Mouse Click**: Click on the button‑like card of the desired algorithm. The selected card will change its background from dark gray to bright cyan with inverted text color for clear distinction.

**Keyboard Shortcut**: Press number keys **1** (DFS), **2** (BFS), **3** (UCS), **4** (Greedy), or **5** (A*) to select instantly.

### Start the Search

Click the large **🚀 START SEARCH** button, or press the **Enter** key on your keyboard.

### Execution

Upon clicking start, the selection window will automatically close, and the corresponding search class (e.g., `DFS.execute()`) will be invoked to solve the maze defined in `maze2.json`.