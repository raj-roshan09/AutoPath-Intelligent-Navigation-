# AutoPath: Smart Navigation System

## 🚗 Project Overview

AutoPath is a simulation-based path-planning project that showcases how an autonomous vehicle can travel from a starting location to a target destination while avoiding obstacles using **Ant Colony Optimization (ACO)**.

The system continuously updates the navigation route when new obstacles appear, making it useful for demonstrating autonomous driving, dynamic path planning, and intelligent routing concepts.

---

## 🎯 Objective

* Create a grid-based simulation for autonomous vehicle navigation
* Determine an efficient route using Ant Colony Optimization
* Adapt to obstacles that are added dynamically during navigation
* Showcase the application of nature-inspired optimization techniques in path planning

---

## 🧠 Algorithm Used

## Ant Colony Optimization (ACO)

Ant Colony Optimization is a nature-inspired optimization technique inspired by the way ants search for food and discover efficient paths.

As ants travel, they leave behind pheromone trails. Routes that provide shorter or better paths gradually accumulate stronger pheromone levels. ACO applies this concept computationally to identify an efficient path between two points.

---

## ⚙️ Features

* Grid-based navigation environment
* Configurable starting and destination points
* Randomly generated static obstacles
* Real-time vehicle movement visualization
* Add new obstacles through mouse interaction
* Automatic path recalculation when obstacles change
* Detection and display of situations where no valid path exists

---

## 🛠️ Technologies Used

* Python
* Pygame
* NumPy

---

## 📂 Project Structure

```text
AutoPath/
│── Main.py
│── ACO.py
│── Grid.py
│── Config.py
│── README.md
```
