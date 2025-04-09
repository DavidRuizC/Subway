
# 🚇 Subway Pathfinding System - AI Search Algorithms (Python)

This project implements several classical **AI search algorithms** to compute optimal paths through a subway network. It supports multiple optimization goals like time, distance, adjacency, and transfers. The system is modular, extensible, and designed with unit testing for validation.

---

## 🧠 Implemented Algorithms

- 🔍 **Depth-First Search (DFS)**
- 🔎 **Breadth-First Search (BFS)**
- 💰 **Uniform Cost Search (UCS)**
- ⭐ **A\* Search** with multiple heuristic preferences
- 📍 **A\* Improved**: Uses spatial coordinates instead of station IDs

---

## 🧩 Project Structure

### 🔹 `SearchAlgorithm.py`
Contains all the pathfinding algorithms and utility functions like expansion, cycle removal, cost calculation, and heuristics.

### 🔹 `SubwayMap.py`
Defines:
- `Map`: Stores station info, connections, and line speeds.
- `Path`: Manages a path's route and costs (`g`, `h`, `f`).

### 🔹 `utils.py`
Helper functions for:
- Reading data files
- Calculating distances
- Printing routes

### 🔹 `TestCases.py`
Comprehensive unit tests using `unittest` to verify all algorithms and subroutines.

### 🔹 `test.py`
Additional tests and experiments with path generation and distance functions.

---

## ⚙️ Setup & Usage

1. Place the city data under:
```
./CityInformation/Lyon_smallCity/
├── Stations.txt
├── Time.txt
├── InfoVelocity.txt
```

2. Run the unit tests:
```bash
python TestCases.py
```

3. Use A\* with coordinates:
```python
from SearchAlgorithm import Astar_improved
path = Astar_improved([80, 100], [100, 240], subway_map)
print(path.route, path.f)
```

---

## 🎯 Preferences in Cost Functions

You can customize search based on 4 preferences:
- `0`: Adjacency
- `1`: Minimum time
- `2`: Minimum distance
- `3`: Minimum transfers

Example:
```python
path = Astar(2, 6, map, type_preference=1)
```

---

## 📈 Example Output

```
Route: [8, 7, 6, 5, 2, 1], Cost: 5
Route: [9, 8, 12, 11, 10, 2, 3], Cost: 55.37
```

---

## ✅ Features

- Modular OOP design
- Supports path comparison (`__eq__`)
- Accurate heuristics via Euclidean distance
- Redundant path pruning for efficiency
- Flexible for various data sources

---

## 📄 License

This project is provided for educational use at UAB.  
Feel free to extend or adapt it for other transport networks!
